from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.forms.formsets import formset_factory

from scaffolding.forms import *
from scaffolding.models import *

def application_list(request):
    fieldFormSet = formset_factory(FieldForm, extra=2)
    if request.method == 'POST':
        formset = fieldFormSet(request.POST)

        if formset.is_valid():
            for form in formset.forms:
                print form.cleaned_data
    else:
        formset = fieldFormSet()
    return direct_to_template(request, 'application/application_list.html', {'formset':fieldFormSet})

def application_detail(request, aid):
    app = get_object_or_404(Application, pk=aid)
    return direct_to_template(request, 'application/application_detail.html',{'app':app})

def application_edit(request, aid):
    return application_base(request, aid)

def application_new(request):
    return application_base(request)

def application_base(request, aid=None):
    app = None
    if aid:
        app = get_object_or_404(Application, pk=aid)
    
    return direct_to_template(request, 'application/application_edit.html', {'app':app})

