from django.template import Library
from scaffolding.utils import *

register = Library()
@register.simple_tag
def doSome(value, arg):
    if value == 'boolean':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="default=&quot;False&quot;" id="id_%(arg)s-options_0" /> default</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_1" /> editable</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_2" /> help text</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_3" /> related name</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_4" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'char':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="choices=[]" id="id_%(arg)s-options_1" /> choices</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="default=&quot;&quot;" id="id_%(arg)s-options_2" /> default</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_3" /> editable</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_4" /> help text</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="max_length=1" id="id_%(arg)s-options_5" /> max length</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_6" /> null</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_7" /> related name</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" value="unique=False" id="id_%(arg)s-options_8" /> unique</label></li><li><label for="id_%(arg)s-options_9"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_9" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'datetime':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="default=datetime.datetime.now" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_4" /> null</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_5" /> related name</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_6" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'file':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="default=&quot;&quot;" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="max_length=255" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_8" /> verbose name</label></li></ul>';
    if value == 'fk':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_1" /> editable</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_2" /> help text</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_3" /> null</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_4" /> related name</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_5" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'int':
       return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="default=0" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="max_length=1" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_8" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'image':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="default=&quot;&quot;" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="max_length=255" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_8" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'pint':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="default=0" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="max_length=1" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_8" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'text':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="default=&quot;&quot;" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="max_length=1" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_7" /> verbose name</label></li></ul>' % {"arg": arg}
    if value == 'default':
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" value="choices=[]" id="id_%(arg)s-options_1" /> choices</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" value="default=&quot;&quot;" id="id_%(arg)s-options_2" /> default</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" value="editable=False" id="id_%(arg)s-options_3" /> editable</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_4" /> help text</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" value="max_length=1" id="id_%(arg)s-options_5" /> max length</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" value="null=True" id="id_%(arg)s-options_6" /> null</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_7" /> related name</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" value="unique=False" id="id_%(arg)s-options_8" /> unique</label></li><li><label for="id_%(arg)s-options_9"><input type="checkbox" name="%(arg)s-options" value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_9" /> verbose name</label></li></ul>' % {"arg": arg}

register.simple_tag(doSome)