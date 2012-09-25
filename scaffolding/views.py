import os
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory

from scaffolding.forms import *
from scaffolding.models import *

def application_list(request):
    apps = Application.objects.filter(status=APPLICATION_STATUS_UNPROCESSED)

    return direct_to_template(request, 'application/application_list.html', {'apps':apps})

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
            formset.instance=clas
            for f in formset.forms:
               a = f.save()
               a.options = f.cleaned_data['options']
               a.save()
               print a.options
            return HttpResponseRedirect(app.get_absolute_url())

    return direct_to_template(request, 'class/class_edit.html', {'app':app, 'clas':clas, 'form':form, 'formset':formset})

def application_process(request, aid):
    app = get_object_or_404(Application, pk=aid)

    if app.status == APPLICATION_STATUS_PROCESSED:
        raise Http404
    #writing the stuff to file
    if not os.path.exists('./%s' % app.name):
        os.makedirs('./%s' % app.name)

    app_model_file =  open('./%s/models.py' % app.name, 'w')

    app_model_file.write('from django.db import models\n')
    
    for c in app.class_set.filter(status=CLASS_STATUS_UNPROCESSED):
        if c.field_set.count():
            app_model_file.write('\nclass %s(models.Model):\n' % c.name)
            for f in c.field_set.filter(status=FIELD_STATUS_UNPROCESSED):
                app_model_file.write('\t%s= models.%s(%s)\n'% (f.name, f.get_type_display(), f.options))

            #still need template and view functions and forms 
    app_model_file.close()
     
    app_view_file = open('./%s/views.py' % app.name, 'w')
    app_view_file.write('from django.http import HttpResponse, HttpResponseRedirect, Http404\nfrom django.views.generic.simple import direct_to_template\nfrom django.shortcuts import get_object_or_404\n\nfrom %s.models import *\nfrom %s.forms import *\n\n' % (app.name, app.name))
    app_view_file.write("def %s_list(request):\n   objects = %s.objects.all()\n    return direct_to_template(request, '%s/%s_list.html', {'objets':objects})" % (app.name.lower(), app.name.title(), app.name.lower(), app.name.lower()))
    app_view_file.close()

    return HttpResponseRedirect('/applications/')
