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

FIELD_TYPES_DIC = {'BooleanField':FIELD_TYPE_BOOLEAN, 'CharField':FIELD_TYPE_CHAR, 
                   'DateTimeField':FIELD_TYPE_DATETIME, 'FileField':FIELD_TYPE_FILE, 
                   'ForeignKey':FIELD_TYPE_FOREIGNKEY, 'IntegerField':FIELD_TYPE_INTEGER,
                   'ImageField':FIELD_TYPE_IMAGE,'PositiveIntegerField':FIELD_TYPE_POSITIVEINTEGER, 
                   'TextField':FIELD_TYPE_TEXT}
                   
#TBD
#                   
#class FieldType(models.Model):
#    name = models.CharField(max_length=200)
#    options = models.ManyToManyField(Option, through='OptionList')
#   
#class Option(models.Model):
#    type = models.CharField(max_length=50)
#    value = models.CharField(max_length=200)
#
#class OptionList(models.Model):
#    field_type = models.ForeignKey(FieldType)
#    option = models.ForeignKey(Option)   
    
class Run(models.Model):    
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)
    
    def __unicode__(self):
        return '%s' % self.id
        
    def get_absolute_url(self): 
        return '/scaffold/%s/' % self.id
        
class Application(models.Model):
    run = models.ForeignKey(Run)
    name = models.CharField(max_length=60, verbose_name='Application Name')
    status = models.CharField(max_length=1, choices=APPLICATION_STATUSES, default=APPLICATION_STATUS_UNPROCESSED)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)

    class Meta: 
        unique_together=(('run', 'name'),)

    def __unicode__(self):
        if self.name:
            return '%s' % (self.name)
        else:
            return '%s' % self.id

    def get_absolute_url(self):
        return '%sapplications/%s/' % (self.run.get_absolute_url(),self.name)
    #    return '/applications/%s/' % (self.id)
    #    return '/applications/%s/' % (self.name)

    def get_other_apps(self):
        return self.run.application_set.exclude(id=self.id)

    def is_processed(self):
        return self.status==APPLICATION_STATUS_PROCESSED

class Class(models.Model):
    name = models.CharField(max_length=60, verbose_name='Class Name')
    application = models.ForeignKey(Application)
    create_view = models.BooleanField(default=False, verbose_name="views.py")
    create_urls = models.BooleanField(default=False, verbose_name="urls.py")
    create_forms = models.BooleanField(default=False, verbose_name="forms.py")
    create_templates = models.BooleanField(default=False, verbose_name="templates")
    create_admin = models.BooleanField(default=False, verbose_name="admin.py")
    extras = models.TextField(blank=True, null=True)
    
    status = models.CharField(max_length=1, choices=CLASS_STATUSES, default=CLASS_STATUS_UNPROCESSED)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)
    
   

    class Meta: 
        unique_together=(('name', 'application'),)

    def __unicode__(self):
        
        return '%s.%s' % (self.application, self.name)

    def get_absolute_url(self):
        return '%sclasses/%s/' % (self.application.get_absolute_url(), self.name)
    def get_edit_absolute_url(self):
        return '%sclasses/%s/edit/' % (self.application.get_absolute_url(), self.name)

    def get_next_class(self):
        try:
            c =  list(self.application.class_set.order_by('id'))
            position = c.index(self)
            return c[position+1] if position != (len(c)-1) else None
        except:
            return None

class Field(models.Model):
    name = models.CharField(max_length=60, verbose_name="Field Name")
    parent_class = models.ForeignKey(Class)
    type = models.CharField(max_length=1, choices=FIELD_TYPES)
    options = models.TextField(blank=True,null=True)
    
    status = models.CharField(max_length=1, choices=FIELD_STATUSES, default=FIELD_STATUS_UNPROCESSED)
    created = models.DateTimeField(default=datetime.datetime.now, editable=False)
 
    class Meta:
        unique_together=(('name', 'parent_class'),)

    def __unicode__(self):
        return '%s.%s' % (self.parent_class, self.name)

    def get_options(self):
        x = self.options.split(',')
        opt = []
        for i in x:
            if not 'fk_name' in i:
                if i:
                    opt.append(i)
        return opt

    def get_fk(self):
        x = self.options.split(',')
        for i in x:
            if 'fk_name' in i:
                return '(%s)' % i.replace('fk_name=','')
        return ''


