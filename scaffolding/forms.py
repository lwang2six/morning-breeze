import re
from django import forms
from scaffolding.models import *

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
    class Meta:
        model = Field
        fields = ['name', 'type']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pattern = re.compile(r'^[a-zA-Z]+([\-_]*[a-zA-Z])?$')
        if not pattern.match(name):
            raise forms.ValidationError('Field names should only contain letters underscore and dash. It should also end with a letter')
        return self.cleaned_data.get('name')
