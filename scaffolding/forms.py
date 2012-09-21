import re
from django import forms
from scaffolding.models import *

class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

    class_num = forms.IntegerField(required=False, initial=0, label='Number of classes', help_text='If unsure, leave it as 0')

    class Meta:
        model = Application
        fields = ['name']

    def clean_class_num(self):
        try:
            if int(self.cleaned_data['class_num']) < 0:
                raise forms.ValidationError(u'Please enter an integer greater or equal to 0')
            else:
                return self.cleaned_data['class_num']
        except:
            raise forms.ValidationError(u'Please enter an integer greater or equal to 0')

class ClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = ['name']

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name', 'type']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pattern = re.compile(r'^[a-zA-Z]+[\-_]*[a-zA-Z]+$')
        if not pattern.match(name):
            raise forms.ValidationError('Field names should only contain letters underscore and dash. It should also end with a letter')
        return self.cleaned_data.get('name')
