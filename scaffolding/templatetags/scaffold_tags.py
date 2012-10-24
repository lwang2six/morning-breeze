import re
from django.template import Library
from scaffolding.utils import *
from scaffolding.models import *

register = Library()

def matches(value, arg):
    if re.compile(arg).match(value):
        return True
    return False
register.filter(matches)

def app_matches(value):
    t = r'/applications/\d+/$'
    return matches(value, t)
register.filter(app_matches)

def class_matches(value, arg):
    t = r"/applications/\d+/classes/%s/$" % arg
    return matches(value, t)
register.filter(class_matches)

def app_edit_matches(value):
    t = r'/applications/\d+/edit/$'
    return matches(value, t)
register.filter(app_edit_matches)

def class_edit_matches(value, arg):
    t = r"/applications/\d+/classes/%s/edit/$" % arg
    return matches(value, t)
register.filter(class_edit_matches)

@register.simple_tag
def doSome(value, arg, new=False):
    check='checked="checked"'
    bl = ch = df = ed = ht = ml = nl = rn = un = vn = ''

    try:
        if value.instance:
            type = value.instance.type
            x = [i.lstrip().rstrip() for i in value.instance.options.split(',')]
            t = [i.split('=')[0] for i in x]
            if u'blank' in t:
                bl = check
            if u'choice' in t:
                ch = check
            if u'default' in t:
                df = check
            if u'editable' in t:
                ed = check
            if u'help_text' in t:
                ht = check
            if u'max_length' in t:
                ml = check
            if u'null' in t:
                nl = check
            if u'related_name' in t:
                rn = check
            if u'unique' in t:
                un = check
            if u'verbose_name' in t:
                vn = check
    except:
        type = None

    if type == FIELD_TYPE_BOOLEAN:
        val = "False"
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=%(val)s" id="id_%(arg)s-options_0" /> default</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_1" /> editable</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_2" /> help text</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_3" /> related name</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_4" /> verbose name</label></li></ul>' % {"arg": arg, "val":val, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn }
    elif type == FIELD_TYPE_CHAR:
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(ch)s value="choices=[]" id="id_%(arg)s-options_1" /> choices</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=&quot;&quot;" id="id_%(arg)s-options_2" /> default</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_3" /> editable</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_4" /> help text</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(ml)s value="max_length=255" id="id_%(arg)s-options_5" disabled="disabled" /> max length *</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_6" /> null</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_7" /> related name</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" %(un)s value="unique=False" id="id_%(arg)s-options_8" /> unique</label></li><li><label for="id_%(arg)s-options_9"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_9" /> verbose name</label></li></ul>' % {"arg": arg, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    elif type == FIELD_TYPE_DATETIME:
        val = "datetime.datetime.now"
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=%(val)s" id="id_%(arg)s-options_1" disabled="disabled"/> default *</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_4" /> null</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_5" /> related name</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_6" /> verbose name</label></li></ul>' % {"arg": arg, "val":val, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    elif type == FIELD_TYPE_FILE:
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=&quot;&quot;" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(ml)s value="max_length=255" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" %(un)s value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" %(vn)s value="upload_to=&quot;.&quot;" id="id_%(arg)s-options_8" disabled="disabled" checked="checked"/> upload to *</label></li><li><label for="id_%(arg)s-options_9"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_9" /> verbose name</label></li></ul>' % {"arg":arg, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    elif type == FIELD_TYPE_FOREIGNKEY:
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_1" /> editable</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_2" /> help text</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_3" /> null</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_4" /> related name</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_5" /> verbose name</label></li></ul>' % {"arg": arg, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    elif type == FIELD_TYPE_INTEGER:
       val = "0"
       return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=%(val)s" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(ml)s value="max_length=255" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" %(un)s value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_8" /> verbose name</label></li></ul>' % {"arg": arg, "val":val, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    elif type == FIELD_TYPE_IMAGE:
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=&quot;&quot;" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(ml)s value="max_length=255" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" %(un)s value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" %(vn)s value="upload_to=&quot;.&quot;" id="id_%(arg)s-options_8" disabled="disabled" checked="checked"/> upload to *</label></li><li><label for="id_%(arg)s-options_9"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_9" /> verbose name</label></li></ul>' % {"arg": arg, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    elif type == FIELD_TYPE_POSITIVEINTEGER:
        val = "0"
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=%(val)s" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(ml)s value="max_length=255" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" %(un)s value="unique=False" id="id_%(arg)s-options_7" /> unique</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_8" /> verbose name</label></li></ul>' % {"arg": arg, "val":val, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    elif type == FIELD_TYPE_TEXT:
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=&quot;&quot;" id="id_%(arg)s-options_1" /> default</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_2" /> editable</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_3" /> help text</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(ml)s value="max_length=255" id="id_%(arg)s-options_4" /> max length</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_5" /> null</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_6" /> related name</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_7" /> verbose name</label></li></ul>' % {"arg": arg, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}
    else:
        return '<div class="id_%(arg)s_choice_list"><ul><li><label for="id_%(arg)s-options_0"><input type="checkbox" name="%(arg)s-options" %(bl)s value="blank=True" id="id_%(arg)s-options_0" /> blank</label></li><li><label for="id_%(arg)s-options_1"><input type="checkbox" name="%(arg)s-options" %(ch)s value="choices=[]" id="id_%(arg)s-options_1" /> choices</label></li><li><label for="id_%(arg)s-options_2"><input type="checkbox" name="%(arg)s-options" %(df)s value="default=&quot;&quot;" id="id_%(arg)s-options_2" /> default</label></li><li><label for="id_%(arg)s-options_3"><input type="checkbox" name="%(arg)s-options" %(ed)s value="editable=False" id="id_%(arg)s-options_3" /> editable</label></li><li><label for="id_%(arg)s-options_4"><input type="checkbox" name="%(arg)s-options" %(ht)s value="help_text=&quot;some help text for this field&quot;" id="id_%(arg)s-options_4" /> help text</label></li><li><label for="id_%(arg)s-options_5"><input type="checkbox" name="%(arg)s-options" %(ml)s value="max_length=255" id="id_%(arg)s-options_5" /> max length</label></li><li><label for="id_%(arg)s-options_6"><input type="checkbox" name="%(arg)s-options" %(nl)s value="null=True" id="id_%(arg)s-options_6" /> null</label></li><li><label for="id_%(arg)s-options_7"><input type="checkbox" name="%(arg)s-options" %(rn)s value="related_name=&quot;some_special_name&quot;" id="id_%(arg)s-options_7" /> related name</label></li><li><label for="id_%(arg)s-options_8"><input type="checkbox" name="%(arg)s-options" %(un)s value="unique=False" id="id_%(arg)s-options_8" /> unique</label></li><li><label for="id_%(arg)s-options_9"><input type="checkbox" name="%(arg)s-options" %(vn)s value="verbose_name=&quot;display name&quot;" id="id_%(arg)s-options_9" /> verbose name</label></li></ul>' % {"arg": arg, 'bl':bl, 'ch':ch, 'df':df, 'ed':ed, 'ht':ht, 'ml':ml, 'nl':nl, 'rn':rn, 'un':un, 'vn':vn}

register.simple_tag(doSome)


def truncate_chars(value, arg):
    if int(arg)+2 < len(value):
        return '%s...' % value[:arg]
    else:
        return value

register.filter(truncate_chars)

