import os
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

    return direct_to_template(request, 'application/application_list.html', {'apps':apps,'processed':processed})

def application_detail(request, aid):
    app = get_object_or_404(Application, pk=aid)
    return direct_to_template(request, 'application/application_detail.html',{'app':app})

def application_edit(request, aid):
    return application_base(request, aid)

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
        classFormSet = inlineformset_factory(Application, Class, form=ClassForm, extra=1, can_delete=False)
        formset = classFormSet(queryset=Class.objects.filter(application=app), instance=app)
  
    if request.method == 'POST':
        form = ApplicationForm(data=request.POST, instance=app)
        formset = classFormSet(request.POST, instance=app)
        if form.is_valid() and formset.is_valid():
            app = form.save()
            formset.instance=app
            formset.save()
            if not aid:
                if app.class_set.count():
                    return HttpResponseRedirect(app.class_set.order_by('id')[0].get_edit_absolute_url())
            return HttpResponseRedirect(app.get_absolute_url())

    return direct_to_template(request, 'application/application_edit.html', {'app':app, 'form':form, 'formset':formset})

def class_edit(request, aid, cname):
    app = get_object_or_404(Application, pk=aid)
    clas = get_object_or_404(Class, application=app, name=cname)
    form = ClassForm(instance=clas)
    formnum = 0 if clas.field_set.count() else 3
    fieldFormSet = inlineformset_factory(Class, Field, form=FieldForm, can_delete=False, extra=formnum)
    formset = fieldFormSet(instance=clas)

    if request.method == 'POST':
        form = ClassForm(data=request.POST, instance=clas)
        formset = fieldFormSet(request.POST, instance=clas)
        if form.is_valid() and formset.is_valid():
            clas = form.save()

            formset.save()
            if request.POST.get('continue'):
                if clas.get_next_class():
                    return HttpResponseRedirect(clas.get_next_class().get_edit_absolute_url())
               
            return HttpResponseRedirect(app.get_absolute_url())

    return direct_to_template(request, 'class/class_edit.html', {'app':app, 'clas':clas, 'form':form, 'formset':formset})

def class_delete(request, aid, cname):
    app = get_object_or_404(Application, pk=aid)
    clas = get_object_or_404(Class, application=app, name=cname)

    if request.method == 'POST':
        if not request.POST.get('cancel'):
            for field in clas.field_set.all():
                field.delete()
            clas.delete()
            return HttpResponseRedirect(app.get_absolute_url())
    return direct_to_template(request, 'class/class_delete.html', {'app':app, 'clas':clas})

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
    count = 0
    for c in app.class_set.filter(status=CLASS_STATUS_UNPROCESSED):
        if c.field_set.count():
            write_model(c, first_class)
            write_views(c, first_class)
            write_forms(c, first_class)
            write_urls(c, first_class, count == c.field_set.count())
            write_admin(c, first_class)
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
