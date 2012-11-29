import re
from django import forms
from django.conf import settings
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple, HiddenInput

from scaffolding.models import *
from scaffolding.utils import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pattern = re.compile(r'^[a-zA-Z]+([\-_][a-zA-Z]+)*$')
        if name == 'new':
            raise forms.ValidationError('Application name cannot be "new"')
            
        if not pattern.match(name):
            raise forms.ValidationError('Application names should only contain letters, underscore and dash. It should also end with a letter')
            
        app = self.instance.run.application_set.filter(name=name)
        if app:
            if not self.instance.id:
                raise forms.ValidationError('An applicajtion with the same name already exists.')
            else:
                if str(app[0].id) != str(self.instance.id):
                    raise forms.ValidationError('An application with the same name already exists.')
        return self.cleaned_data.get('name')

class ApplicationFieldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplicationFieldForm, self).__init__(*args, **kwargs)
        self.fields['app_name'] = forms.ChoiceField(label="Application", choices=[(str(app.id), str(app.name)) for app in self.instance.run.application_set.all()], initial=self.instance.id)
    class Meta:
        model = Application
        exclude = ['id', 'name', 'run', 'created', 'status']

    def clean_app_name(self):
        app_name = self.cleaned_data.get('app_name')
        try:
            return Application.objects.get(id=app_name)
        except:
            return None

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        exclude = ['id','application', 'status', 'created']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pattern = re.compile(r'^[a-zA-Z]+([\-_][a-zA-Z]+)*$')
        if not pattern.match(name):
            raise forms.ValidationError('Class names should only contain letters, underscore and dash. It should also end with a letter')

        if self.instance.application_id:
            clas = self.instance.application.class_set.filter(name=name)
            if clas:
                if not self.instance.id:
                    raise forms.ValidationError('An class with the same name already exists.')
                else:
                    if clas[0].id != self.instance.id:
                        raise forms.ValidationError('A class with the same name already exists.')

        return self.cleaned_data.get('name').lstrip().rstrip()

class ClassFieldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassFieldForm, self).__init__(*args, **kwargs)
        self.fields['app_name'] = forms.ChoiceField(label="Application", choices=[(str(app.id), str(app.name)) for app in self.instance.application.run.application_set.all()], initial=self.instance.application.id)

    class Meta:
        model = Class
        exclude = ['id', 'application', 'create_view', 'create_urls', 'create_forms', 'create_templates', 'create_admin', 'status', 'created']

    def clean_name(self):
        name = self.cleaned_data['name']
        pattern = re.compile(r'^[a-zA-Z]+([\-_][a-zA-Z]+)*$')
        if not pattern.match(name):
            raise forms.ValidationError('Class names should only contain letters, underscore and dash. It should also end with a letter')

        clas = self.instance.application.class_set.filter(name=name)
        if clas:
                if not self.instance.id:
                    raise forms.ValidationError('An class with the same name already exists.')
                else:
                    if clas[0].id != self.instance.id:
                        raise forms.ValidationError('A class with the same name already exists.')

        return self.cleaned_data.get('name').lstrip().rstrip()

    def clean_app_name(self):
            app_name = self.cleaned_data.get('app_name')

            app = Application.objects.get(id=app_name)

            if str(self.instance.application.id) != str(app_name):
                if app.class_set.filter(name=self.cleaned_data.get('name')):
                   raise forms.ValidationError('The choosen application already has a class with the same name.')
            print 'here'
            return app


class FieldForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FieldForm,self).__init__(*args,**kwargs)
        initial_options=[]
        option_choice = FIELD_OPTIONS_DEFAULT

        if self.instance.id is not None:
            if self.instance.type == FIELD_TYPE_FOREIGNKEY:
                fk_initial = None
                initial_options = []
                for i in self.instance.options.split(','):
                    if 'fk_name=' in i:
                        fk_initial = i.lstrip().rstrip().split('fk_name=')[1]
                    else:
                        initial_options.append(i.lstrip().rstrip())                
                #empty fk name is being caught in the clean form, cannot be required because if the field type changes, it will throw a validation error
                self.fields['option_fk_name'] = forms.CharField(label="Foreign Key Class", initial=fk_initial, required=False)
            else:
                initial_options = [i.lstrip().rstrip() for i in self.instance.options.split(',')]

            stype = self.instance.type
            if stype:
                if stype == FIELD_TYPE_BOOLEAN:
                    option_choice = FIELD_OPTIONS_BOOL
                if stype == FIELD_TYPE_CHAR:
                    option_choice = FIELD_OPTIONS_CHAR
                if stype == FIELD_TYPE_DATETIME:
                    option_choice = FIELD_OPTIONS_DATETIME
                if stype == FIELD_TYPE_FILE:
                    option_choice = FIELD_OPTIONS_FILE
                if stype == FIELD_TYPE_FOREIGNKEY:
                    option_choice = FIELD_OPTIONS_FK
                if stype == FIELD_TYPE_INTEGER:
                    option_choice = FIELD_OPTIONS_INTEGER
                if stype == FIELD_TYPE_IMAGE:
                    option_choice = FIELD_OPTIONS_IMAGE
                if stype == FIELD_TYPE_POSITIVEINTEGER:
                    option_choice = FIELD_OPTIONS_PINT
                if stype == FIELD_TYPE_TEXT:   
                    option_choice = FIELD_OPTIONS_TEXT

        self.fields['options'] = forms.MultipleChoiceField(label='Options', choices=FIELD_OPTIONS_DEFAULT, widget=CheckboxSelectMultiple, initial=initial_options, required=False)

    class Meta:
        model = Field
        fields = ['name', 'type']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pattern = re.compile(r'^[a-zA-Z]+([\-_][a-zA-Z]+)*$')
        if not pattern.match(name):
            raise forms.ValidationError('Field names should only contain letters, underscore and dash. It should also end with a letter')
        return self.cleaned_data.get('name').lstrip().rstrip()

    def clean_option_fk_name(self):
        try:
            if self.cleaned_data['type'] == FIELD_TYPE_FOREIGNKEY:
                fkc = self.cleaned_data.get('option_fk_name')
                if not fkc:
                    fkc = self.data['%s-options_fk_name' % self.prefix]
                if fkc:
                    x = "fk_name=%s" % fkc.strip()
                    self.instance.options += ", %s" % x if self.instance.options else x
                    return fkc
                else:
                    raise forms.ValidationError("Foreign Key Name cannot be empty.")
            else:
                return None
        except:
            return None

    def clean_options(self):
        stype = self.cleaned_data.get('type')
        def_op = 'default=""'

        required_options = []

        #boolean
        if stype == '1':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_BOOL_SET):
                raise forms.ValidationError("One of the selected options is not allowed for boolean field")

        #char
        if stype == '2':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_CHAR_SET):
                raise forms.ValidationError("One of the selected options is not allowed for char field")
            required_options.append(FIELD_OPTION_MAX_LENGTH)

        #datetime
        if stype == '3':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_DATETIME_SET):
                raise forms.ValidationError("One of the selected options is not allowed for datetime field")
            required_options.append(FIELD_OPTION_DEFAULT_DATETIME_NOW)
        #file
        if stype == '4':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_FILE_SET):
                raise forms.ValidationError("One of the selected options is not allowed for file field")
            required_options.append(FIELD_OPTION_UPLOADTO)

        #fk change to classes
        if stype == '5':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_FK_SET):
                raise forms.ValidationError("One of the selected options is not allowed for foreign key")

        #integer
        if stype == '6':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_INTEGER_SET):
                raise forms.ValidationError("One of the selected options is not allowed for integer field")
            #required_options.append(FIELD_OPTION_DEFAULT_ZERO)
        #image
        if stype == '7':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_IMAGE_SET):
                raise forms.ValidationError("One of the selected options is not allowed for image field")
            required_options.append(FIELD_OPTION_UPLOADTO)

        #positiveinteger
        if stype == '8':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_PINT_SET):
                raise forms.ValidationError("One of the selected options is not allowed for positive integer field")
            #required_options.append(FIELD_OPTION_DEFAULT_ZERO)
        #text
        if stype == '9':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_TEXT_SET):
                raise forms.ValidationError("One of the selected options is not allowed for text field")
        
        x = ''
        x = self.cleaned_data.get('options') + required_options
        x = set(x)

        out = ''
        for i in x:
            if out:
                out = '%s, %s' % (i, out)
            else:
                out = '%s' % i

        self.instance.options = out
        self.clean_option_fk_name()
        return self.instance.options

class DatabaseForm(forms.Form):
    db_choices = settings.DATABASES.keys()
    #not sure why i remove scaffold_temp
    db_choices.remove('scaffold_temp')
    db_name = forms.ChoiceField(label="Database to Scaffold", choices=[('','---------------')]+[(str(db), str(db)) for db in db_choices], required=False)
    
    db_location = forms.FileField(label="Database Location", required=False)
    db = forms.CharField(label="Database to source the data", help_text="database to model after, it has to be one of the ones inside the DATABASES", required=False)
    
    def clean_db(self):
        name = self.cleaned_data.get('db')

        if self.cleaned_data.get('db_name') and name:
            raise forms.ValidationError('Please choose either to scaffold an existing database OR choose a .sql file but not both!')
        if name:
            pattern = re.compile(r'^[a-zA-Z0-9\-_]+$')
            if not pattern.match(name):
                raise forms.ValidationError('Database name should only consist of letters, numbers, dashes and underscores')
            return name
        else:
            return None

    def clean_db_name(self):
        db_name = self.cleaned_data.get('db_name')

        if db_name and (self.cleaned_data.get('db_location') or self.cleaned_data.get('db')):
            raise forms.ValidationError("Please choose either to scaffold an existing database OR choose a .sql file")

        if db_name:
            if not settings.DATABASES.has_key(self.cleaned_data.get('db_name')):
                raise forms.ValidationError("Please select a valid database, if the database is not listed please include it inside your settings.py's DATABASES.")
            return self.cleaned_data.get('db_name')
        else:
            return None
    
    def clean_db_location(self):
        print self.files

        return self.cleaned_data.get('db_location')










