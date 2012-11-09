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

def scaffold(request):
    return direct_to_template(request, 'scaffold_home.html', { 'path':request.path})

def scaffold_list(request):
    run = Run.objects.all()
    return direct_to_template(request, 'scaffold_list.html', {'runs':run,  'path':request.path})

def application_list(request, rid):
    run = get_object_or_404(Run, pk=rid)
    apps = Application.objects.filter(run=run, status=APPLICATION_STATUS_UNPROCESSED)
    processed = Application.objects.filter(run=run, status=APPLICATION_STATUS_PROCESSED)

    return direct_to_template(request, 'application/application_list.html', {'apps':apps,'run':run,'processed':processed, 'path':request.path})

def application_detail(request, rid, aname):
    run = get_object_or_404(Run, pk=rid)
    app = get_object_or_404(Application, run=run, name=aname)
    return direct_to_template(request, 'application/application_detail.html',{'run':run, 'app':app, 'path':request.path})

def application_edit(request, rid, aname):
    return application_base(request, rid, aname)

def application_new(request, rid=None):
    return application_base(request, rid)

def application_base(request, rid=None, aname=None):
    run = app = None
    form = ApplicationForm()
    classFormSet = inlineformset_factory(Application, Class, form=ClassForm, extra=3, can_delete=False)
    formset = classFormSet()
    if rid:
        run = get_object_or_404(Run, pk=rid)
    else:
        run = Run()

    if aname:
        app = get_object_or_404(Application, run=run, name=aname)
        form = ApplicationForm(instance=app)
        classFormSet = inlineformset_factory(Application, Class, form=ClassForm, extra=0, can_delete=False)
        formset = classFormSet(queryset=Class.objects.filter(application=app), instance=app)

    if request.method == 'POST':
        if request.POST.get('cancel'):
            if run.id:
                if app:
                    return HttpResponseRedirect(app.get_absolute_url())
                else:
                    return HttpResponseRedirect(run.get_absolute_url())
            else:
                return HttpResponseRedirect('/scaffold/runs')

        if not aname:
            app = Application(run=run)

        form = ApplicationForm(data=request.POST, instance=app)
        formset = classFormSet(request.POST, instance=app)
        
        if form.is_valid():
            run.save()
            form.instance.run = run
            app = form.save()
            formset = classFormSet(request.POST, instance=app)
            if formset.is_valid():
                for i in formset.forms:
                    try:
                        i.clean_name()
                        i.save()
                    except:
                        pass

                if request.POST.get('continue'):
                    if app.class_set.count():
                        return HttpResponseRedirect(app.class_set.order_by('id')[0].get_edit_absolute_url())

                #if request.POST.get('add_another_app'):
                #    return HttpResponseRedirect('%sapplications/new/' % run.get_absolute_url())
                #if request.POST.get('save'):
                return HttpResponseRedirect(app.get_absolute_url())

    return direct_to_template(request, 'application/application_edit.html', {'run':run, 'app':app, 'form':form, 'formset':formset, 'path':request.path})

def application_delete(request, rid, aname):
    run = get_object_or_404(Run, pk=rid)
    app = get_object_or_404(Application, run=run, name=aname)
    
    if request.method == 'POST':
        if not request.POST.get('cancel'):
            for clas in app.class_set.all():
                for field in clas.field_set.all():
                    field.delete()
                clas.delete()
            app.delete()
        return HttpResponseRedirect('applications')
    return direct_to_template(request, 'application/application_delete.html', {'run':run, 'app':app, 'path':request.path})               

def class_detail(request, rid, aname, cname):
    run = get_object_or_404(Run, pk=rid)
    app = get_object_or_404(Application, run=run, name=aname)
    clas = get_object_or_404(Class, application=app, name=cname)

    return direct_to_template(request, 'class/class_detail.html', {'run':run, 'app':app, 'clas':clas, 'path':request.path})

def class_edit(request, rid, aname, cname):
    run = get_object_or_404(Run, pk=rid)
    app = get_object_or_404(Application, run=run, name=aname)
    clas = get_object_or_404(Class, application=app, name=cname)
    #appform = ApplicationFieldForm(instance=app)
    form = ClassFieldForm(instance=clas)
    formnum = 0 if clas.field_set.count() else 3
    fieldFormSet = inlineformset_factory(Class, Field, form=FieldForm, can_delete=False, extra=formnum)
    formset = fieldFormSet(instance=clas)

    if request.method == 'POST':
        form = ClassFieldForm(data=request.POST, instance=clas)
        formset = fieldFormSet(request.POST, instance=clas)
        #appform = ApplicationFieldForm(data=request.POST, instance=app)

        if request.POST.get('cancel'):
            return HttpResponseRedirect(clas.get_absolute_url())

        if form.is_valid() and formset.is_valid():
            clas = form.save()
            formset.save()

            if form.cleaned_data.get('app_name'):
                app = form.cleaned_data.get('app_name')

                clas.application = app
                clas.save()

            if request.POST.get('continue'):
                if clas.get_next_class():
                    return HttpResponseRedirect(clas.get_next_class().get_edit_absolute_url())

            return HttpResponseRedirect(clas.get_absolute_url())

    return direct_to_template(request, 'class/class_edit.html', {'run':run, 'app':app, 'clas':clas, 'path':request.path, 'form':form, 'formset':formset})

def class_delete(request, rid, aname, cname):
    run = get_object_or_404(Run, pk=rid)
    app = get_object_or_404(Application, run=run, name=aname)
    clas = get_object_or_404(Class, application=app, name=cname)

    if request.method == 'POST':
        if not request.POST.get('cancel'):
            for field in clas.field_set.all():
                field.delete()
            clas.delete()
            return HttpResponseRedirect(app.get_absolute_url())
    return direct_to_template(request, 'class/class_delete.html', {'run':run, 'app':app, 'clas':clas, 'path':request.path})

def application_confirmation(request, rid, aname):
    run = get_object_or_404(Run, pk=rid)
    app = get_object_or_404(Application, run=run, name=aname)

    return direct_to_template(request, 'application/application_confirmation.html', {'run':run, 'app':app, 'path':request.path})

def application_process(request, rid, aname):
    run = get_object_or_404(Run, pk=rid)
    app = get_object_or_404(Application, run=run, name=aname)

    if request.method == 'POST':
        if not request.POST.get('cancel'):
            #if app.status == APPLICATION_STATUS_PROCESSED:
            #    raise Http404
            app_name = app.name.lower()
            #writing the stuff to file
            if not os.path.exists('./%s' % app_name):
                os.makedirs('./%s' % app_name)
                app_init_file = open('./%s/__init__.py' % app_name, 'w')
                app_init_file.close()
             
            first_class=True
            count = 1
            # create all classes without fk first.
            for c in list(app.class_set.exclude(field__type=FIELD_TYPE_FOREIGNKEY))+list(app.class_set.filter(field__type=FIELD_TYPE_FOREIGNKEY).distinct()):
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
                    for field in c.field_set.filter(status=FIELD_STATUS_UNPROCESSED).distinct():
                        field.status = FIELD_STATUS_PROCESSED
                        field.save()
                    c.save()
             
            app.status = APPLICATION_STATUS_PROCESSED
            app.save()
            return HttpResponseRedirect(run.get_absolute_url())
    return HttpResponseRedirect(app.get_absolute_url())

def scaffold_database(request):
    db_form = DatabaseForm()

    if request.method == 'POST':
        db_form = DatabaseForm(data=request.POST, files=request.FILES)

        if db_form.is_valid():

            if db_form.cleaned_data['db_name']:
                x = process_sql(db_form.cleaned_data['db_name'])
                return HttpResponseRedirect(x.get_absolute_url())
            else:
                d_file = db_form.cleaned_data['db_location']
                db_location = './scaffolding/media/%s' % d_file.name
                db_file = open(db_location, 'w')
                for  chunk in d_file.chunks():
                    db_file.write(chunk)

                db_file.close()
                
                #assumin the default database's user account can create and modify databases
                database = settings.DATABASES['default']
                cur = connections['default'].cursor()
                x = commands.getoutput("mysql -u %s -p%s -e 'create database if not exists scaffold_temp;'" % (database['USER'], database['PASSWORD']))
                #cur.execute('CREATE DATABASE IF NOT EXISTS scaffold_temp;')
                db_exist = cur.execute('SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME="%s";' % db_form.cleaned_data.get('db'))

                x =  commands.getoutput('mysql -u %s -p%s scaffold_temp < %s' % (database['USER'], database['PASSWORD'], db_location))
                db = db_form.cleaned_data.get('db')
                if db:
                    x = commands.getoutput("mysql -u %s -p%s -e 'create database if not exists %s;'" % (database['USER'], database['PASSWORD'], db))
                    x =  commands.getoutput('mysql -u %s -p%s %s < %s' % (database['USER'], database['PASSWORD'], db, db_location))

                return HttpResponseRedirect(process_sql().get_absolute_url())
    return direct_to_template(request, 'database/database_form.html', {'db_form':db_form, 'path':request.path})
    
def process_sql(database_name='scaffold_temp'):
    run = Run()
    run.save()
    x = commands.getoutput('python manage.py inspectdb --database %s' % database_name)
    have_class = False
    clas = extra = ''
    
    app = Application(run=run, name='Unknown')
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

                    for j in opt_list:
                        z = ''
                        if type == 'ForeignKey':                           
                            z = 'fk_name=%s' % j
                        else:
                            z = j

                        if '=' in z:
                            if opt:
                                opt = '%s, %s' % (opt, z)
                            else:
                                opt = z

                    try:     
                        type = FIELD_TYPES_DIC[type]
                    except:
                        type = '9'

                    field = Field(name=name.lstrip().rstrip(), parent_class=clas, type=type, options=opt)
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
            


