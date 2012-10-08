from django.conf.urls.defaults import patterns

urlpatterns = patterns('scaffolding.views',
    (r'^applications/(?P<aid>\d+)/edit/$', 'application_edit'),
    (r'^applications/(?P<aid>\d+)/classes/(?P<cname>[a-zA-Z]+([\-_]*[a-zA-Z]*)?)/edit/$', 'class_edit'),
    (r'^applications/(?P<aid>\d+)/classes/(?P<cname>[a-zA-Z]+([a-zA-Z\-_]*[a-zA-Z]+)?)/delete/$', 'class_delete'),
    (r'^applications/(?P<aid>\d+)/classes/(?P<cname>[a-zA-Z]+([a-zA-Z\-_]*[a-zA-Z]+)?)/$', 'class_detail'),
    (r'^applications/(?P<aid>\d+)/$', 'application_detail'),
    (r'^applications/(?P<aid>\d+)/process/$', 'application_process'),
    (r'^applications/new/$', 'application_new'),
    (r'^applications/$', 'application_list'),
)
