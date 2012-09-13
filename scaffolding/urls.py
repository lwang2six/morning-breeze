from django.conf.urls.defaults import patterns

urlpatterns = patterns('scaffolding.views',
    (r'^applications/(?P<aid>\d+)/edit/$', 'application_edit'),
    (r'^applications/(?P<aid>\d+)/$', 'application_detail'),
    (r'^applications/new/$', 'application_new'),
    (r'^applications/$', 'application_list'),
)
