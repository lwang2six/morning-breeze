import os
import commands
from django.db import connections
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory

from scaffolding.forms import *
from scaffolding.models import *
from scaffolding.write_file import *

def application_list(request):
    apps = Application.objects.filter(status=APPLICATION_STATUS_UNPROCESSED)
    processed = Application.objects.filter(status=APPLICATION_STATUS_PROCESSED)

    return direct_to_template(request, 'application/application_list.html', {'apps':apps,'processed':processed, 'path':request.path})

def application_detail(request, aid):
    app = get_object_or_404(Application, pk=aid)
    return direct_to_template(request, 'application/application_detail.html',{'app':app, 'path':request.path})

def application_edit(request, aid):
    return application_base(request,aid)

def application_new(request):
    return application_base(request)

def application_base(request, aid=None):
    app = None
    form = ApplicationForm()
    classFormSet = inlineformset_factory(Application, Class, form=ClassForm, extra=3, can_delete=False)
    formset = classFormSet()

    if aid:
        app = get_object_or_404(Application, pk=aid)
        form = ApplicationForm(instance=app)
        classFormSet = inlineformset_factory(Application, Class, form=ClassForm, extra=0, can_delete=False)
        formset = classFormSet(queryset=Class.objects.filter(application=app), instance=app)

    if request.method == 'POST':
        form = ApplicationForm(data=request.POST, instance=app)
        formset = classFormSet(request.POST, instance=app)
        print form.errors
        print formset.errors
        if form.is_valid() and formset.is_valid():
            app = form.save()
            formset.instance=app
            formset.save()
            if not aid:
                if app.class_set.count():
                    return HttpResponseRedirect(app.class_set.order_by('id')[0].get_edit_absolute_url())
            return HttpResponseRedirect(app.get_absolute_url())

    return direct_to_template(request, 'application/application_edit.html', {'app':app, 'form':form, 'formset':formset, 'path':request.path})

def application_delete(request, aid=None):
    app = get_object_or_404(Application, pk=aid)
    
    if request.method == 'POST':
        if not request.POST.get('cancel'):
            for clas in app.class_set.all():
                for field in clas.field_set.all():
                    field.delete()
                clas.delete()
            app.delete()
        return HttpResponseRedirect('applications')
    return direct_to_template(request, 'application/application_delete.html', {'app':app, 'path':request.path})               

def class_detail(request, aid, cname):
    app = get_object_or_404(Application, pk=aid)
    clas = get_object_or_404(Class, application=app, name=cname)

    return direct_to_template(request, 'class/class_detail.html', {'app':app, 'clas':clas, 'path':request.path})

def class_edit(request, aid, cname):
    app = get_object_or_404(Application, pk=aid)
    clas = get_object_or_404(Class, application=app, name=cname)
    form = ClassFieldForm(instance=clas)
    formnum = 0 if clas.field_set.count() else 3
    fieldFormSet = inlineformset_factory(Class, Field, form=FieldForm, can_delete=False, extra=formnum)
    formset = fieldFormSet(instance=clas)


    if request.method == 'POST':
        form = ClassFieldForm(data=request.POST, instance=clas)
        formset = fieldFormSet(request.POST, instance=clas)
        if form.is_valid() and formset.is_valid():
            clas = form.save()

            formset.save()
            if request.POST.get('continue'):
                if clas.get_next_class():
                    return HttpResponseRedirect(clas.get_next_class().get_edit_absolute_url())
               
            return HttpResponseRedirect(app.get_absolute_url())

    return direct_to_template(request, 'class/class_edit.html', {'app':app, 'clas':clas, 'path':request.path, 'form':form, 'formset':formset})

def class_delete(request, aid, cname):
    app = get_object_or_404(Application, pk=aid)
    clas = get_object_or_404(Class, application=app, name=cname)

    if request.method == 'POST':
        if not request.POST.get('cancel'):
            for field in clas.field_set.all():
                field.delete()
            clas.delete()
            return HttpResponseRedirect(app.get_absolute_url())
    return direct_to_template(request, 'class/class_delete.html', {'app':app, 'clas':clas, 'path':request.path})

def application_process(request, aid):
    app = get_object_or_404(Application, pk=aid)

    #if app.status == APPLICATION_STATUS_PROCESSED:
    #    raise Http404
    app_name = app.name.lower()
    #writing the stuff to file
    if not os.path.exists('./%s' % app_name):
        os.makedirs('./%s' % app_name)
        app_init_file = open('./%s/__init__.py' % app_name, 'w')
        app_init_file.close()
        os.makedirs('./%s/templates' % app_name)
     
    first_class=True
    count = 1
    for c in app.class_set.all():
        if c.field_set.count():
            write_model(c, first_class)
            if c.create_view:
                write_views(c, first_class)
            if c.create_forms:
                write_forms(c, first_class)
            if c.create_urls:
                write_urls(c, first_class, count == c.field_set.count())
            if c.create_admin:
                write_admin(c, first_class)
            if c.create_templates:
                write_templates(c)

            first_class=False
            count = count + 1
            c.status = CLASS_STATUS_PROCESSED
            for field in c.field_set.filter(status=FIELD_STATUS_UNPROCESSED):
                field.status = FIELD_STATUS_PROCESSED
                field.save()
            c.save()
     
    app.status = APPLICATION_STATUS_PROCESSED
    app.save()

    return HttpResponseRedirect('/applications/')
    
    
def scaffold_database(request):
    db_form = DatabaseForm()
    dbdump_form = DatabaseDumpForm()
    if request.method == 'POST':
        db_form = DatabaseForm(data=request.POST)
        dbdump_form = DatabaseDumpForm(data=request.POST)

        if db_form.is_valid() and dbdump_form.is_valid():
            print 'choose only one please'
        else:
            if db_form.is_valid():
                x = process_sql(db_form.cleaned_data['db_name'])
                return HttpResponseRedirect(x.get_absolute_url())
                
            #assumin the default database's user account can create and modify databases
            #database = settings.DATABASES['default']
            #cur = connections['default'].cursor()
            #cur.execute('DROP DATABASE IF EXISTS scaffold_temp;')
            #cur.execute('CREATE DATABASE scaffold_temp;')
            #db_exist = cur.execute('SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME="%s";' % form.cleaned_data.get('db_name'))
            #if form.cleaned_data['db'] and form.cleaned_data['db_location']:
            #    cur.execute('create database if not exists %s;' % form.cleaned_data.get('db'))
            #    x =  commands.getoutput('mysql -u %s -p%s %s < %s' % (database['USER'], database['PASSWORD'], form.cleaned_data['db'], form.cleaned_data['db_location']))
    
    #process_sql()
    return direct_to_template(request, 'database/database_form.html', {'db_form':db_form, 'dbdump_form':dbdump_form})
    
def process_sql(database_name='scaffold_temp'):
    print database_name
    x = commands.getoutput('python manage.py inspectdb --database %s' % database_name)
    have_class = False
    clas = extra = ''
    
    app = Application(name='Unknown')
    app.save()
    for i in x.split('\n'):
        if 'class' in i and '(models.Model):' in i:
            have_class = True
            if extra:
                #current clas would be refering to the previous one not the new one.            
                clas.extras = extra
                clas.save()
            extra = ''
            c_name = i.replace('class','').replace('(models.Model):','').lstrip().rstrip()
            clas = Class(name=c_name, application=app)
            clas.save()

        else:
            if have_class and not i.startswith('#'):
                f = i.lstrip().rstrip().split('models.')
                if len(f) > 1:
                    name = f[0].lstrip().rstrip().split('=')[0]
                    type, opt = f[1].lstrip().rstrip().split('(')
                    opt = opt[:-1]
                    opt_list = opt.split(',')
                    opt = ''
                    for i in opt_list:
                        if '=' in i:
                            if type == 'ForeignKey':
                                z = 'fk=%s' % i
                            else:
                                z = i
                            if opt:
                                opt = '%s, %s' % (opt, z)
                            else:
                                opt = z

                    try:     
                        type = FIELD_TYPES_DIC[type]
                    except:
                        type = '9'

                    field = Field(name=name, parent_class=clas, type=type, options=opt)
                    field.save()
                elif len(f) == 1 and not i.startswith('#'):
                    if extra:
                        extra = '%s\n%s' % (extra, i)
                    else:
                        extra = i
    if clas:
        clas.extras = extra
        clas.save()                        
                 
    return app       
            


