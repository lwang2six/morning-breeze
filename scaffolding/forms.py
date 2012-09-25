import re
from django import forms
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple

from scaffolding.models import *

FIELD_OPTION_BLANK = 'blank=True'
FIELD_OPTION_CHOICES = 'choices=[]'
FIELD_OPTION_DEFAULT = 'default=""'
FIELD_OPTION_EDITABLE = 'editable=False'
FIELD_OPTION_HELP_TEXT = 'help_text="some help text for this field"'
FIELD_OPTION_MAX_LENGTH = 'max_length=1'
FIELD_OPTION_NULL = 'null=True'
FIELD_OPTION_RELATED_NAME = 'related_name="some_special_name"'
FIELD_OPTION_UNIQUE = 'unique=False'
FIELD_OPTION_VERBOSE_NAME = 'verbose_name="display name"'

FIELD_OPTIONS =(
            (FIELD_OPTION_BLANK , 'blank'),
            (FIELD_OPTION_CHOICES , 'choices'),
            (FIELD_OPTION_DEFAULT , 'default'),
            (FIELD_OPTION_EDITABLE, 'editable'), 
            (FIELD_OPTION_HELP_TEXT, 'help text'),
            (FIELD_OPTION_MAX_LENGTH, 'max length'),
            (FIELD_OPTION_NULL, 'null'), 
            (FIELD_OPTION_RELATED_NAME, 'related name'), 
            (FIELD_OPTION_UNIQUE, 'unique'),
            (FIELD_OPTION_VERBOSE_NAME, 'verbose name'), 
        )

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
  
    options = forms.MultipleChoiceField(label='Options', choices=FIELD_OPTIONS, widget=CheckboxSelectMultiple, required=False)

    class Meta:
        model = Field
        fields = ['name', 'type']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pattern = re.compile(r'^[a-zA-Z]+([\-_]*[a-zA-Z])?$')
        if not pattern.match(name):
            raise forms.ValidationError('Field names should only contain letters underscore and dash. It should also end with a letter')
        return self.cleaned_data.get('name')

    def clean_options(self):
        stype = self.cleaned_data.get('type')
        #boolean
        if stype == '1':
            if not set(self.cleaned_data.get('options')).issubset([FIELD_OPTION_DEFAULT, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_VERBOSE_NAME]):
                raise forms.ValidationError("One of the selected options is not allowed for boolean field")

        #char
        if stype == '2':
            if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK, FIELD_OPTION_CHOICES, FIELD_OPTION_DEFAULT, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE, FIELD_OPTION_VERBOSE_NAME])):
                raise forms.ValidationError("One of the selected options is not allowed for char field")

        #datetime
        if stype == '3':
            if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK, FIELD_OPTION_DEFAULT, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_VERBOSE_NAME])):
                raise forms.ValidationError("One of the selected options is not allowed for char field")

        #file
        if stype == '4':
            if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE, FIELD_OPTION_VERBOSE_NAME])):
                raise forms.ValidationError("One of the selected options is not allowed for char field")

        #fk change to classes
        #if stype == '5':
        #    if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE, FIELD_OPTION_VERBOSE_NAME])):
        #        raise forms.ValidationError("One of the selected options is not allowed for char field")

        #integer
        if stype == '6':
            if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK, FIELD_OPTION_DEFAULT, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_VERBOSE_NAME])):
                raise forms.ValidationError("One of the selected options is not allowed for char field")

        #image
        if stype == '7':
            if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK,  FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE, FIELD_OPTION_VERBOSE_NAME])):
                raise forms.ValidationError("One of the selected options is not allowed for char field")

        #positiveinteger
        if stype == '8':
            if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK, FIELD_OPTION_DEFAULT, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_VERBOSE_NAME])):
                raise forms.ValidationError("One of the selected options is not allowed for char field")

        #text
        if stype == '9':
            if not set(self.cleaned_data.get('options')).issubset(set([FIELD_OPTION_BLANK, FIELD_OPTION_DEFAULT, FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE, FIELD_OPTION_VERBOSE_NAME])):
                raise forms.ValidationError("One of the selected options is not allowed for char field")
        
        x = ''
        for i in self.cleaned_data.get('options'):
            x += '%s, ' % i
        return x[:-2]



