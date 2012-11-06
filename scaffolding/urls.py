from django.conf.urls.defaults import patterns

urlpatterns = patterns('scaffolding.views',
    (r'^scaffold/(?P<rid>\d+)/applications/new/$', 'application_new'),
    (r'^scaffold/(?P<rid>\d+)/applications/$', 'application_list'),
    (r'^scaffold/new/$', 'application_new'),
    (r'^scaffold/(?P<rid>\d+)/applications/(?P<aname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/edit/$', 'application_edit'),
    (r'^scaffold/(?P<rid>\d+)/applications/(?P<aname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/classes/(?P<cname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/edit/$', 'class_edit'),
    (r'^scaffold/(?P<rid>\d+)/applications/(?P<aname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/classes/(?P<cname>[a-zA-Z]+([a-zA-Z\-_]*[a-zA-Z]+)?)/delete/$', 'class_delete'),
    (r'^scaffold/(?P<rid>\d+)/applications/(?P<aname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/classes/(?P<cname>[a-zA-Z]+([a-zA-Z\-_]*[a-zA-Z]+)?)/$', 'class_detail'),
    (r'^scaffold/(?P<rid>\d+)/applications/(?P<aname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/$', 'application_detail'),
    (r'^scaffold/(?P<rid>\d+)/applications/(?P<aname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/process/$', 'application_process'),

    (r'^scaffold/(?P<rid>\d+)/applications/(?P<aname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/delete/$', 'application_delete'),
    (r'^scaffold/(?P<rid>\d+)/$', 'application_list'),
    (r'^scaffold/runs/$', 'scaffold_list'),
    (r'^scaffold/$', 'scaffold'),

    (r'^scaffold/database/$', 'scaffold_database'),
)
