import datetime
from django.db import models

APPLICATION_STATUS_PROCESSED = 'P'
APPLICATION_STATUS_UNPROCESSED = 'U'
APPLICATION_STATUSES = (
    (APPLICATION_STATUS_PROCESSED, 'Processed'),
    (APPLICATION_STATUS_UNPROCESSED, 'Un-Processed'),
)

CLASS_STATUS_PROCESSED = 'P'
CLASS_STATUS_UNPROCESSED = 'U'
CLASS_STATUSES = (
    (CLASS_STATUS_PROCESSED, 'Processed'),
    (CLASS_STATUS_UNPROCESSED, 'Un-Processed'),
)

FIELD_STATUS_PROCESSED = 'P'
FIELD_STATUS_UNPROCESSED = 'U'
FIELD_STATUSES = (
    (FIELD_STATUS_PROCESSED, 'Processed'),
    (FIELD_STATUS_UNPROCESSED, 'Un-Processed'),
)

FIELD_TYPE_BOOLEAN = '1'
FIELD_TYPE_CHAR = '2'
FIELD_TYPE_DATETIME = '3'
FIELD_TYPE_FILE = '4'
FIELD_TYPE_FOREIGNKEY = '5'
FIELD_TYPE_INTEGER = '6'
FIELD_TYPE_IMAGE = '7'
FIELD_TYPE_POSITIVEINTEGER = '8' 
FIELD_TYPE_TEXT = '9'
FIELD_TYPES = (
    (FIELD_TYPE_BOOLEAN, 'BooleanField'),
    (FIELD_TYPE_CHAR, 'CharField'),
    (FIELD_TYPE_DATETIME, 'DateTimeField'),
    (FIELD_TYPE_FILE, 'FileField'),
    (FIELD_TYPE_FOREIGNKEY, 'ForeignKey'),
    (FIELD_TYPE_INTEGER, 'IntegerField'),
    (FIELD_TYPE_IMAGE, 'ImageField'),
    (FIELD_TYPE_POSITIVEINTEGER, 'PositiveIntegerField'),
    (FIELD_TYPE_TEXT, 'TextField'),
)
class Application(models.Model):
    name = models.CharField(max_length=30, verbose_name='Application Name')
    status = models.CharField(max_length=1, choices=APPLICATION_STATUSES, default=APPLICATION_STATUS_UNPROCESSED)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)

    def __unicode__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return '/applications/%s/' % self.id 

class Class(models.Model):
    name = models.CharField(max_length=30, verbose_name='Class Name')
    application = models.ForeignKey(Application)
    status = models.CharField(max_length=1, choices=CLASS_STATUSES, default=CLASS_STATUS_UNPROCESSED)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)

    class Meta: 
        unique_together=(('name', 'application'),)

    def __unicode__(self):
        return '%s.%s' % (self.application, self.name)

class Field(models.Model):
    name = models.CharField(max_length=30)
    parent_class = models.ForeignKey(Class)
    type = models.CharField(max_length=1, choices=FIELD_TYPES)
    options = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=1, choices=FIELD_STATUSES, default=FIELD_STATUS_UNPROCESSED)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)
 
    class Meta:
        unique_together=(('name', 'parent_class'),)

    def __unicode__(self):
        return '%s.%s' % (self.parent_class, self.name)


