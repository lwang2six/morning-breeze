from django.http import HttpResponse, HttpResponseRedirect
from django.views.genric.simple import direct_to_template
from django.shortcuts import get_object_or_404


from scaffolding.models import *

def application_list(request):
    return direct_to_template(request, 'application/application_list.html', {})

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
    
    return direct_to_template(request, 'appliation/application_edit.html', {'app':app})

