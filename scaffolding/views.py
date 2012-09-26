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
    app_name = app.name.lower()
    #writing the stuff to file
    if not os.path.exists('./%s' % app_name):
        os.makedirs('./%s' % app_name)
        os.makedirs('./%s/templates' % app_name)

    #making models.py
    app_model_file =  open('./%s/models.py' % app_name, 'w')
    app_model_file.write('from django.db import models\n')

    #making views.py
    app_view_file = open('./%s/views.py' % app_name, 'w')
    app_view_file.write('from django.http import HttpResponse, HttpResponseRedirect, Http404\n')
    app_view_file.write('from django.views.generic.simple import direct_to_template\n')
    app_view_file.write('from django.shortcuts import get_object_or_404\n')
    app_view_file.write('from %s.models import *\n' % app_name)
    app_view_file.write('from %s.forms import *\n\n' % app_name)
    
    #making forms.py
    app_form_file = open('./%s/forms.py' % app_name, 'w')
    app_form_file.write('from django import forms\n')
    app_form_file.write('from %s.models import *\n\n' % app_name)

    #making urls.py
    app_url_file = open('./%s/urls.py' % app_name, 'w')
    app_url_file.write('from django.conf.urls.defaults import *\n')
    app_url_file.write('urlpatterns = patterns('',\n')

    for c in app.class_set.filter(status=CLASS_STATUS_UNPROCESSED):
        if c.field_set.count():
            class_name =  c.name.lower()
            app_model_file.write('class %s(models.Model):\n' % class_name.title())
            for f in c.field_set.filter(status=FIELD_STATUS_UNPROCESSED):
                app_model_file.write('    %s= models.%s(%s)\n'% (f.name.lower(), f.get_type_display(), f.options))
            app_model_file.write('    def __unicode__(self):\n')
            x = "        return '%%s - %%s' % (self.id, self."
            x += "%s)\n" % c.field_set.all()[0].name
            print x
            app_model_file.write(x)
            app_model_file.write('    def get_absolute_url(self):\n')
            x = "        return '/%s/" % class_name
            x += "%%s % self.id)\n"
            app_model_file.write(x)

#function for view
            app_view_file.write('def %s_list(request):\n' % class_name)
            app_view_file.write('    objects = %s.objects.all()\n' % class_name.title())
            app_view_file.write("    return direct_to_template(request, '%s/%s_list.html', {'objets':objects})\n" % (class_name, class_name))
            app_view_file.write('\n')
            app_view_file.write("def %s_detail(request, oid):\n" % class_name)
            app_view_file.write("    object = get_object_or_404(%s, pk=oid)\n" % class_name.title())
            app_view_file.write("    return direct_to_template(request, '%s/%s_detail.html',{'object':object})\n" % (class_name, class_name))
            app_view_file.write('\n')
            app_view_file.write("def %s_new(request):\n" % class_name)
            app_view_file.write('    form = %sForm()\n' % class_name.title())
            app_view_file.write('    if request.POST:\n')
            app_view_file.write('        if request.POST.get("cancel"):\n')
            app_view_file.write('            return HttpResponseRedirect("/%s/")\n' % class_name)        
            app_view_file.write('        form = %sForm(data=request.POST)\n' % class_name.title())
            app_view_file.write('        if form.is_valid():\n')
            app_view_file.write('            object = form.save()\n')
            app_view_file.write('            return HttpResponseRedirect(object.get_absolute_url())\n')
            app_view_file.write("    return direct_to_template('%s/%s_new.html', {'form':form})\n" % (class_name, class_name))
            app_view_file.write('\n')
            app_view_file.write('def %s_edit(request, oid):\n' % class_name)
            app_view_file.write('    object = get_object_or_404(%s, pk=oid)\n' % class_name.title())
            app_view_file.write('    form = %sForm(instance=object)\n' % class_name.title())
            app_view_file.write('    if request.POST:\n')
            app_view_file.write('        form = %sForm(data=request.POST, instance=object)\n' % class_name.title())
            app_view_file.write('        if form.is_valid():\n')
            app_view_file.write('            form.save()\n')
            app_view_file.write('            return HttpResponseRedirect(object.get_absolute_url())\n')
            app_view_file.write("    return direct_to_template('%s/%s_edit.html', {'form':form, 'object':object})\n" % (class_name, class_name))
            app_view_file.write('\n')
            app_view_file.write('def %s_delete(request,oid):\n' % class_name)
            app_view_file.write('    object = get_object_or_404(%s, pk=oid)\n' % class_name.title())
            app_view_file.write('    if request.POST:\n')
            app_view_file.write("        if request.POST.get('cancel'):\n")
            app_view_file.write("            return HttpResponseRedirect(object.get_absolute_url())\n")
            app_view_file.write('        else:\n')
            app_view_file.write('            object.delete()\n')
            app_view_file.write("            return HttpResponseRedirect('/%s/')\n" % class_name)
            app_view_file.write("    return direct_to_response(request, '%s/%s_delete.html', {'object':object})\n" % (class_name, class_name))
            app_view_file.write('\n')

            app_form_file.write('class %sForm(forms.ModelForm):\n' % class_name.title())
            app_form_file.write('    def __init__(self, *args, **kwargs):\n')
            app_form_file.write('        super(%sForm, self).__init__(*args, **kwargs)\n\n' % class_name.title())
            app_form_file.write('    class Meta:\n')
            app_form_file.write('        model = %s\n' % class_name.title())
            app_form_file.write('        #fields = []\n')
            app_form_file.write('        #exclude = []\n')

            app_url_file.write("    (r'^%s/new/$', '%s.views.%s_new'\n" % (class_name, app_name, class_name))
            app_url_file.write("    (r'^%s/(?P<oid>\d+)/edit/$', '%s.views.%s_edit'\n" % (class_name, app_name, class_name))
            app_url_file.write("    (r'^%s/(?P<oid>\d+)/delete/$', '%s.views.%s_delete'\n" % (class_name, app_name, class_name))
            app_url_file.write("    (r'^%s/(?P<oid>\d+)/$', '%s.views.%s_details'\n" % (class_name, app_name, class_name))
            app_url_file.write("    (r'^%s/$', '%s.views.%s_list'\n" % (class_name, app_name, class_name))


            if not os.path.exists('./%s/templates/%s' % (app_name, class_name)):
                os.makedirs('./%s/templates/%s' % (app_name, class_name))
            temp_root = './%s/templates/%s/%s_' % (app_name, class_name, class_name)

            temp_file = open('%slist.html' % (temp_root), 'w')
            x = '{% extends "'
            x += '%s/base_%s.html"' % (class_name, class_name)
            x += ' %}\n'
            temp_file.write(x)
            temp_file.write('{% block content %}\n')
            temp_file.write('    <div>\n')
            temp_file.write('        <h1>%s List</h1>\n' % class_name)
            temp_file.write('        <ul>\n')
            temp_file.write('            {% for object in objects %}\n')
            temp_file.write('               <li><a href="{{object.get_absolute_url}}">{{object}}</a></li>\n')
            temp_file.write('            {% endfor %}\n')
            temp_file.write('        </ul>\n')
            temp_file.write('    </div>\n')
            temp_file.write('{% endblock content %}\n')
            temp_file.close()

            temp_file = open('%sdetail.html' % temp_root, 'w')
            x = '{% extends "'
            x += '%s/base_%s.html"' % (class_name, class_name)
            x += ' %}\n'
            temp_file.write(x)
            temp_file.write('{% block content %}\n')
            temp_file.write('    <div>\n')
            for i in c.field_set.all():
                temp_file.write('    %s: {{object.%s}}<br/>\n' % (i.name.title(), i.name.lower()))
            temp_file.write('    </div>\n')
            temp_file.write('{% endblock content %}\n')

            temp_file = open('%snew.html' % temp_root, 'w')
            x = '{% extends "'
            x += '%s/base_%s.html"' % (class_name, class_name)
            x += ' %}\n'
            temp_file.write(x)
            temp_file.write('{% block content %}\n')
            temp_file.write('    <div>\n')
            temp_file.write('        {% if form.errors %}\n')
            temp_file.write('            <span>Please complete the required field(s)</span>\n')
            temp_file.write('        {% endif %}\n')
            temp_file.write('    </div>\n')
            temp_file.write('    <div>\n')
            temp_file.write('        <form action="" method=post>{% csrf_token%}\n')
            temp_file.write('            <fieldset>\n')
            temp_file.write('                {{ form }}\n')
            temp_file.write('            </fieldset>\n')
            temp_file.write('            <input type="submit" value="Submit" name="save" class="button"/>\n')
            temp_file.write('            <input type="submit" value="Cancel" name="cancel" class="button"/>\n')
            temp_file.write('        </form>\n')
            temp_file.write('    </div>\n')
            temp_file.write('{% endblock content %}\n')

            temp_file = open('%sedit.html' % temp_root, 'w')
            x = '{% extends "'
            x += '%s/base_%s.html"' % (class_name, class_name)
            x += ' %}\n'
            temp_file.write(x)
            temp_file.write('{% block content %}\n')
            temp_file.write('    <h1>{{object}}:</h1>\n')
            temp_file.write('    <div>\n')
            temp_file.write('        {% if form.errors %}\n')
            temp_file.write('            <span>Please complete the required field(s)</span>\n')
            temp_file.write('        {% endif %}\n')
            temp_file.write('    </div>\n')
            temp_file.write('    <div>\n')
            temp_file.write('        <form action="" method=post>{% csrf_token%}\n')
            temp_file.write('            <fieldset>\n')
            temp_file.write('                {{ form }}\n')
            temp_file.write('            </fieldset>\n')
            temp_file.write('            <input type="submit" value="Submit" name="save" class="button"/>\n')
            temp_file.write('            <input type="submit" value="Cancel" name="cancel" class="button"/>\n')
            temp_file.write('        </form>\n')
            temp_file.write('    </div>\n')
            temp_file.write('{% endblock content %}\n')

            temp_file = open('%sdelete.html' % temp_root, 'w')
            x = '{% extends "'
            x += '%s/base_%s.html"' % (class_name, class_name)
            x += ' %}\n'
            temp_file.write(x)
            temp_file.write('{% block content %}\n')
            temp_file.write('    <div>\n')
            temp_file.write('        <h2>Are you sure you want to delete: <a href="{{object.get_absolute_url}}">{{object}}</a></h2>\n')
            temp_file.write('    </div>\n')
            temp_file.write('    <form method="post" action="">{% csrf token %}\n')
            temp_file.write('        <input type="submit" value="Submit" name="save" class="button"/>\n')
            temp_file.write('        <input type="submit" value="Cancel" name="cancel" class="button"/>\n')
            temp_file.write('    </form>\n')
            temp_file.write('{% endblock content %}\n')

    app_url_file.write(')')
    app_url_file.close()
    app_view_file.close()
    app_model_file.close()

    return HttpResponseRedirect('/applications/')
