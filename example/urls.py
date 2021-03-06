from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
     (r'^', include('scaffolding.urls')),
     (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # allow django to serve htdocs site media
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
