import os
from scaffolding.models import * 

def write_model(class_object, first_class=False):
    file_name = './%s/models.py' % class_object.application.name.lower()
    write_type = 'a'
    first_line = '\n'

    if first_class:
        write_type = 'w'
        first_line = 'from django.db import models\n\n'
    model_file = open(file_name, write_type)
    model_file.write(first_line)

    class_name =  class_object.name.lower()
    model_file.write('class %s(models.Model):\n' % class_name.title())

    for field in class_object.field_set.filter(status=FIELD_STATUS_UNPROCESSED):
        opts =  field.options.split('fk_name=')

        if len(opts) == 2:
            if not opts[0]:
                opts = opts[1].lstrip().rstrip()
            else:
                opts = '%s, %s' % (opts[1].lstrip().rstrip(), opts[0].lstrip().rstrip())
        else:
            opts = opts[0].lstrip().rstrip()

        if opts:
            if opts[-1] == ',':
                opts = opts[:-1]
            
        model_file.write('    %s= models.%s(%s)\n'% (field.name.lower(), field.get_type_display(), opts))

    model_file.write('\n    def __unicode__(self):\n')
    x = "        return '%s - %s' % (self.id, self."
    x += "%s)\n" % class_object.field_set.all()[0].name.lower()
    model_file.write(x)

    model_file.write('\n    def get_absolute_url(self):\n')
    x = "        return '/%s/" % class_name
    x += "%s' % self.id\n"
    model_file.write(x)

    model_file.close()

def write_views(class_object, first_class=False):
    app_name = class_object.application.name.lower()
    class_name =  class_object.name.lower()

    file_name = './%s/views.py' % app_name
    write_type = 'a'
    first_line = '\n'

    if first_class:
        write_type = 'w'
        first_line = "from django.http import HttpResponse, HttpResponseRedirect, Http404\n" +\
        "from django.views.generic.simple import direct_to_template\n" +\
        "from django.shortcuts import get_object_or_404\n" +\
        "from %s.models import *\n" % app_name +\
        "from %s.forms import *\n\n" % app_name 

    view_file = open(file_name, write_type)
    view_file.write(first_line)

    view_file.write('def %s_list(request):\n' % class_name)
    view_file.write('    objects = %s.objects.all()\n' % class_object.name)
    view_file.write("    return direct_to_template(request, '%s/%s_list.html', {'objets':objects})\n" % (class_name, class_name))
    view_file.write('\n')
    view_file.write("def %s_detail(request, oid):\n" % class_name)
    view_file.write("    object = get_object_or_404(%s, pk=oid)\n" % class_object.name)
    view_file.write("    return direct_to_template(request, '%s/%s_detail.html',{'object':object})\n" % (class_name, class_name))
    view_file.write('\n')
    view_file.write("def %s_new(request):\n" % class_name)
    view_file.write('    form = %sForm()\n' % class_object.name)
    view_file.write('    if request.POST:\n')
    view_file.write('        if request.POST.get("cancel"):\n')
    view_file.write('            return HttpResponseRedirect("/%s/")\n' % class_name)        
    view_file.write('        form = %sForm(data=request.POST)\n' % class_object.name)
    view_file.write('        if form.is_valid():\n')
    view_file.write('            object = form.save()\n')
    view_file.write('            return HttpResponseRedirect(object.get_absolute_url())\n')
    view_file.write("    return direct_to_template(request, '%s/%s_new.html', {'form':form})\n" % (class_name, class_name))
    view_file.write('\n')
    view_file.write('def %s_edit(request, oid):\n' % class_name)
    view_file.write('    object = get_object_or_404(%s, pk=oid)\n' % class_object.name)
    view_file.write('    form = %sForm(instance=object)\n' % class_name.title())
    view_file.write('    if request.POST:\n')
    view_file.write('        form = %sForm(data=request.POST, instance=object)\n' % class_object.name)
    view_file.write('        if form.is_valid():\n')
    view_file.write('            form.save()\n')
    view_file.write('            return HttpResponseRedirect(object.get_absolute_url())\n')
    view_file.write("    return direct_to_template(request, '%s/%s_edit.html', {'form':form, 'object':object})\n" % (class_name, class_name))
    view_file.write('\n')
    view_file.write('def %s_delete(request,oid):\n' % class_name)
    view_file.write('    object = get_object_or_404(%s, pk=oid)\n' % class_object.name)
    view_file.write('    if request.POST:\n')
    view_file.write("        if request.POST.get('cancel'):\n")
    view_file.write("            return HttpResponseRedirect(object.get_absolute_url())\n")
    view_file.write('        else:\n')
    view_file.write('            object.delete()\n')
    view_file.write("            return HttpResponseRedirect('/%s/')\n" % class_name)
    view_file.write("    return direct_to_template(request, '%s/%s_delete.html', {'object':object})\n" % (class_name, class_name))
    view_file.write('\n')

    view_file.close()

def write_forms(class_object, first_class):
    file_name = './%s/forms.py' % class_object.application.name.lower()
    write_type = 'a'
    first_line = '\n'
    class_name =  class_object.name.lower()

    if first_class:
        write_type = 'w'
        first_line = 'from django import forms\n' +\
                     'from %s.models import *\n\n' % class_object.application.name.lower()

    form_file = open(file_name, write_type)
    form_file.write(first_line)

    form_file.write('class %sForm(forms.ModelForm):\n' % class_object.name)
    form_file.write('    def __init__(self, *args, **kwargs):\n')
    form_file.write('        super(%sForm, self).__init__(*args, **kwargs)\n\n' % class_object.name)
    form_file.write('    class Meta:\n')
    form_file.write('        model = %s\n' % class_object.name)
    form_file.write('        #fields = []\n')
    form_file.write('        #exclude = []\n')

    form_file.close()

def write_urls(class_object, first_class=False, last_class=False):
    class_name = class_object.name.lower()
    app_name = class_object.application.name.lower()
    file_name = './%s/urls.py' % app_name
    write_type = 'a'
    first_line = '\n'

    if first_class:
        write_type = 'w'
        first_line = "from django.conf.urls.defaults import *\n\n" +\
                     "urlpatterns = patterns('',\n"

    url_file = open(file_name, write_type)
    url_file.write(first_line)

    url_file.write("    (r'^%s/new/$', '%s.views.%s_new'),\n" % (class_name, app_name, class_name))
    url_file.write("    (r'^%s/(?P<oid>\d+)/edit/$', '%s.views.%s_edit'),\n" % (class_name, app_name, class_name))
    url_file.write("    (r'^%s/(?P<oid>\d+)/delete/$', '%s.views.%s_delete'),\n" % (class_name, app_name, class_name))
    url_file.write("    (r'^%s/(?P<oid>\d+)/$', '%s.views.%s_detail'),\n" % (class_name, app_name, class_name))
    url_file.write("    (r'^%s/$', '%s.views.%s_list'),\n" % (class_name, app_name, class_name))

    if last_class:
        url_file.write(')')

    url_file.close()

def write_admin(class_object, first_class):
    file_name = './%s/admin.py' % class_object.application.name.lower()
    write_type = 'a'
    first_line = '\n'
    class_name =  class_object.name.lower()

    if first_class:
        write_type = 'w'
        first_line = 'from django.contrib import admin\n' +\
                     'from %s.models import *\n\n' % class_object.application.name.lower()

    admin_file = open(file_name, write_type)
    admin_file.write(first_line)

    admin_file.write('class %sAdmin(admin.ModelAdmin):\n' % class_object.name)
    admin_file.write("    list_display = ('id',)\n\n")
    admin_file.write('admin.site.register(%s, %sAdmin)\n' % (class_object.name, class_object.name))
    admin_file.close()

def make_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def write_template_base(class_object):
    class_name = class_object.name.lower()
    temp_root = './%s/templates/%s/%s_' % (class_object.application.name.lower(), class_name, class_name)
    temp_file = open('%sbase.html' % temp_root, 'w')

    temp_file.write('<head>')
    x = '    <title>%s' % class_name
    x +=' {% if object %}- {{object}}{% endif %}</title>'
    temp_file.write(x)
    temp_file.write('</head>')
    temp_file.write('<body>')
    temp_file.write('    {% block content %}\n')
    temp_file.write('    {% endblock content %}\n')
    temp_file.write('</body>')
    temp_file.close()

def write_template_new(class_object):
    class_name = class_object.name.lower()
    temp_root = './%s/templates/%s/%s_' % (class_object.application.name.lower(), class_name, class_name)
    temp_file = open('%slist.html' % (temp_root), 'w')

    x = '{% '
    x += 'extends "%s/%s_base.html"' % (class_name, class_name)
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
    temp_file.write('            <input type="submit" value="Save" name="save" class="button"/>\n')
    temp_file.write('            <input type="submit" value="Cancel" name="cancel" class="button"/>\n')
    temp_file.write('        </form>\n')
    temp_file.write('    </div>\n')
    temp_file.write('{% endblock content %}\n')
    temp_file.close()

def write_template_list(class_object):
    class_name = class_object.name.lower()
    temp_root = './%s/templates/%s/%s_' % (class_object.application.name.lower(), class_name, class_name)
    temp_file = open('%slist.html' % (temp_root), 'w')

    x = '{% '
    x += 'extends "%s/%s_base.html"' % (class_name, class_name)
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

def write_template_detail(class_object):
    class_name = class_object.name.lower()
    temp_root = './%s/templates/%s/%s_' % (class_object.application.name.lower(), class_name, class_name)
    temp_file = open('%sdetail.html' % temp_root, 'w')

    x = '{% '
    x += 'extends "%s/%s_base.html"' % (class_name, class_name)
    x += ' %}\n'
    temp_file.write(x)
    temp_file.write('{% block content %}\n')
    temp_file.write('    <div>\n')

    for field in class_object.field_set.all():
        temp_file.write('    %s: {{object.%s}}<br/>\n' % (field.name.title(), field.name.lower()))

    temp_file.write('    </div>\n')
    temp_file.write('{% endblock content %}\n')
    temp_file.close()

def write_template_edit(class_object):
    class_name = class_object.name.lower()
    temp_root = './%s/templates/%s/%s_' % (class_object.application.name.lower(), class_name, class_name)
    temp_file = open('%sedit.html' % temp_root, 'w')

    x = '{% '
    x += 'extends "%s/%s_base.html"' % (class_name, class_name)
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
    temp_file.write('            <input type="submit" value="Save" name="save" class="button"/>\n')
    temp_file.write('            <input type="submit" value="Cancel" name="cancel" class="button"/>\n')
    temp_file.write('        </form>\n')
    temp_file.write('    </div>\n')
    temp_file.write('{% endblock content %}\n')
    temp_file.close()

def write_template_delete(class_object):
    class_name = class_object.name.lower()
    temp_root = './%s/templates/%s/%s_' % (class_object.application.name.lower(), class_name, class_name)
    temp_file = open('%sdelete.html' % temp_root, 'w')

    x = '{% '
    x += 'extends "%s/%s_base.html"' % (class_name, class_name)
    x += ' %}\n'
    temp_file.write(x)

    temp_file.write('{% block content %}\n')
    temp_file.write('    <div>\n')
    temp_file.write('        <h2>Are you sure you want to delete: <a href="{{object.get_absolute_url}}">{{object}}</a></h2>\n')
    temp_file.write('    </div>\n')
    temp_file.write('    <form method="post" action="">{% csrf_token %}\n')
    temp_file.write('        <input type="submit" value="Delete" name="delete" class="button"/>\n')
    temp_file.write('        <input type="submit" value="Cancel" name="cancel" class="button"/>\n')
    temp_file.write('    </form>\n')
    temp_file.write('{% endblock content %}\n')
    temp_file.close()

def write_templates(class_object):
    make_folder('./%s/templates/%s' % (class_object.application.name.lower(), class_object.name.lower()))
    write_template_base(class_object)
    write_template_new(class_object)
    write_template_list(class_object)
    write_template_detail(class_object)
    write_template_edit(class_object)
    write_template_delete(class_object)

