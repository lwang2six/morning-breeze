from django.contrib import admin
from django.conf import settings

from scaffolding.models import *

if settings.DEBUG:
    class ApplicationAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'status')

    class ClassAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'application', 'status')

    class FieldAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'parent_class', 'type', 'status')

    admin.site.register(Application, ApplicationAdmin)
    admin.site.register(Class, ClassAdmin)
    admin.site.register(Field,FieldAdmin)
