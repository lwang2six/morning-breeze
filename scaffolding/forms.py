import re
from django import forms
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple, HiddenInput

from scaffolding.models import *
from scaffolding.utils import *

class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Application
        fields = ['name']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pattern = re.compile(r'^[a-zA-Z]+([\-_]*[a-zA-Z]*)?$')
        if not pattern.match(name):
            raise forms.ValidationError('Field names should only contain letters underscore and dash. It should also end with a letter')
        return self.cleaned_data.get('name')

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
                        fk_initial = i.lstrip().rstrip().strip('fk_name=').title()
                    else:
                        initial_options.append(i.lstrip().rstrip())                    
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
        pattern = re.compile(r'^[a-zA-Z]+([\-_]*[a-zA-Z])?$')
        if not pattern.match(name):
            raise forms.ValidationError('Field names should only contain letters underscore and dash. It should also end with a letter')
        return self.cleaned_data.get('name')

    def clean_option_fk_name(self):
        if self.cleaned_data['type'] == FIELD_TYPE_FOREIGNKEY:
            fkc = self.cleaned_data.get('option_fk_name')
            if not fkc:
                fkc = self.data['%s-options_fk_name' % self.prefix]
            if fkc:
                self.instance.options += ", fk_name=%s" % fkc.strip().title()
                return fkc
            else:
                raise forms.ValidationError("Foreign Key Name cannot be empty.")
        else:
            return None

    def clean_options(self):
        stype = self.cleaned_data.get('type')
        def_op = 'default=""'
        try:
            print 'weeeee'
            print self.cleaned_data['options']
        except:
            print 'inside here'
        #boolean
        if stype == '1':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_BOOL_SET):
                raise forms.ValidationError("One of the selected options is not allowed for boolean field")
            def_op = "default=False"

        #char
        if stype == '2':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_CHAR_SET):
                raise forms.ValidationError("One of the selected options is not allowed for char field")

        #datetime
        if stype == '3':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_DATETIME_SET):
                raise forms.ValidationError("One of the selected options is not allowed for datetime field")
            def_op = "default=datetime.datetime.now"
        #file
        if stype == '4':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_FILE_SET):
                raise forms.ValidationError("One of the selected options is not allowed for file field")

        #fk change to classes
        if stype == '5':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_FK_SET):
                raise forms.ValidationError("One of the selected options is not allowed for foreign key")

        #integer
        if stype == '6':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_INTEGER_SET):
                raise forms.ValidationError("One of the selected options is not allowed for integer field")
            def_op = "default=0"

        #image
        if stype == '7':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_IMAGE_SET):
                raise forms.ValidationError("One of the selected options is not allowed for image field")

        #positiveinteger
        if stype == '8':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_PINT_SET):
                raise forms.ValidationError("One of the selected options is not allowed for positive integer field")
            def_op = "default=0"
        #text
        if stype == '9':
            if not set(self.cleaned_data.get('options')).issubset(FIELD_OPTIONS_TEXT_SET):
                raise forms.ValidationError("One of the selected options is not allowed for text field")
        
        x = ''

        for i in self.cleaned_data.get('options'):
            if "default" in i:
                x += '%s, ' % def_op
            else:  
                x += '%s, ' % i
        self.instance.options = x[:-2]
        self.clean_option_fk_name()
        return self.instance.options



