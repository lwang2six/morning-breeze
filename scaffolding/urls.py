from django.conf.urls.defaults import patterns

urlpatterns = patterns('scaffolding.views',
    (r'^applications/(?P<aid>\d+)/edit/$', 'application_edit'),
    (r'^applications/(?P<aid>\d+)/edit/classes/(?P<cname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/$', 'class_edit'),
    (r'^applications/(?P<aid>\d+)/$', 'application_detail'),
    (r'^applications/(?P<aid>\d+)/process/$', 'application_process'),
    (r'^applications/new/$', 'application_new'),
    (r'^applications/$', 'application_list'),
)
