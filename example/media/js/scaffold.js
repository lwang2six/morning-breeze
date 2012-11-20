(function($){
        yay = function(field_prefix, field_type, count) {
                var id_field_type = '#id_'+field_prefix+'-type';
                var class_fk_name_row = '#'+field_prefix+'-option_fk_name_row';
                var id_field_prefix = 'id_' + field_prefix;
                var field_set_option = field_prefix + '-options';
                var x = field_type;
                var field;

                var even = '""';
                var v = +count-1;
                if (v%2 === 0){
                  even = 'class="tr_gray" ';
                }
 
                if(x=='BooleanField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="' + id_field_prefix + '-options_0"><input type="checkbox" name='+ field_set_option+'" value="default=False" id="id_' + field_set_option +'_0" /> default</label></li><li><label for="id_' + field_set_option +'_1"><input type="checkbox" name="'+field_set_option+ '" value="editable=False" id="id_' + field_set_option + '_1" /> editable</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_2" /> help text</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_3" /> related name</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_4" /> verbose name</label></li></ul>';
                }
                else if(x == 'CharField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="choices=[]" id="id_' + field_set_option + '_1" /> choices</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="default=&quot;&quot;" id="id_' + field_set_option + '_2" /> default</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_3" /> editable</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_4" /> help text</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="max_length=255" id="id_' + field_set_option + '_5" checked="checked" disabled="disabled"/> max length *</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_6" /> null</label></li><li><label for="id_' + field_set_option + '_7"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_7" /> related name</label></li><li><label for="id_' + field_set_option + '_8"><input type="checkbox" name="' + field_set_option + '" value="unique=False" id="id_' + field_set_option + '_8" /> unique</label></li><li><label for="id_' + field_set_option + '_9"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_9" /> verbose name</label></li></ul>';
                }
                else if(x == 'DateTimeField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="default=datetime.datetime.now" id="id_' + field_set_option + '_1" checked="checked" disabled="disabled"/> default *</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_2" /> editable</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_3" /> help text</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_4" /> null</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_5" /> related name</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_6" /> verbose name</label></li></ul>';
                }
                else if(x == 'FileField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="default=&quot;&quot;" id="id_' + field_set_option + '_1" /> default</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_2" /> editable</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_3" /> help text</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="max_length=255" id="id_' + field_set_option + '_4" /> max length</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_5" /> null</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_6" /> related name</label></li><li><label for="id_' + field_set_option + '_7"><input type="checkbox" name="' + field_set_option + '" value="unique=False" id="id_' + field_set_option + '_7" /> unique</label></li><li><label for="id_' + field_set_option + '_8"><input type="checkbox" name="' + field_set_option + '" value="upload_to=&quot;.&quot;" id="id_' + field_set_option + '_8" disabled="disabled" checked="checked" /> upload to *</label></li><li><label for="id_' + field_set_option + '_9"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_9" /> verbose name</label></li></ul>';
                }
                else if(x == "ForeignKey"){
                    $("#" + field_prefix + "-type_row").after('<tr id="' + field_prefix + '-option_fk_name_row" ' + even +'><th><label for="' + id_field_prefix + '-option_fk_name">Foreign Key Class</label></th><td><input type="text" name="'+field_set_option+'_fk_name" id="' + id_field_prefix + '-option_fk_name"/></td></tr>');
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_1" /> editable</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_2" /> help text</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_3" /> null</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_4" /> related name</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_5" /> verbose name</label></li></ul>';
                }
                else if(x == 'IntegerField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="default=0" id="id_' + field_set_option + '_1" /> default</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_2" /> editable</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_3" /> help text</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="max_length=255" id="id_' + field_set_option + '_4" /> max length</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_5" /> null</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_6" /> related name</label></li><li><label for="id_' + field_set_option + '_7"><input type="checkbox" name="' + field_set_option + '" value="unique=False" id="id_' + field_set_option + '_7" /> unique</label></li><li><label for="id_' + field_set_option + '_8"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_8" /> verbose name</label></li></ul>';
                }
                else if(x == 'ImageField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="default=&quot;&quot;" id="id_' + field_set_option + '_1" /> default</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_2" /> editable</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_3" /> help text</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="max_length=255" id="id_' + field_set_option + '_4" /> max length</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_5" /> null</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_6" /> related name</label></li><li><label for="id_' + field_set_option + '_7"><input type="checkbox" name="' + field_set_option + '" value="unique=False" id="id_' + field_set_option + '_7" /> unique</label></li><li><label for="id_' + field_set_option + '_8"><input type="checkbox" name="' + field_set_option + '" value="upload_to=&quot;.&quot;" id="id_' + field_set_option + '_8" disabled="disabled" checked="checked" /> upload to *</label></li><li><label for="id_' + field_set_option + '_9"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_9" /> verbose name</label></li></ul>';
                }
                else if(x == 'PositiveIntegerField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="default=0" id="id_' + field_set_option + '_1" /> default</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_2" /> editable</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_3" /> help text</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="max_length=255" id="id_' + field_set_option + '_4" /> max length</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_5" /> null</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_6" /> related name</label></li><li><label for="id_' + field_set_option + '_7"><input type="checkbox" name="' + field_set_option + '" value="unique=False" id="id_' + field_set_option + '_7" /> unique</label></li><li><label for="id_' + field_set_option + '_8"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_8" /> verbose name</label></li></ul>';
                }
                else if(x == 'TextField'){
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="default=&quot;&quot;" id="id_' + field_set_option + '_1" /> default</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_2" /> editable</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_3" /> help text</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="max_length=255" id="id_' + field_set_option + '_4" /> max length</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_5" /> null</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_6" /> related name</label></li><li><label for="id_' + field_set_option + '_7"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_7" /> verbose name</label></li></ul>';
                }
                else {
                    $(class_fk_name_row).remove();
                    field = '<div id="' + id_field_prefix + '_choice_list"><ul><li><label for="id_' + field_set_option + '_0"><input type="checkbox" name="' + field_set_option + '" value="blank=True" id="id_' + field_set_option + '_0" /> blank</label></li><li><label for="id_' + field_set_option + '_1"><input type="checkbox" name="' + field_set_option + '" value="choices=[]" id="id_' + field_set_option + '_1" /> choices</label></li><li><label for="id_' + field_set_option + '_2"><input type="checkbox" name="' + field_set_option + '" value="default=&quot;&quot;" id="id_' + field_set_option + '_2" /> default</label></li><li><label for="id_' + field_set_option + '_3"><input type="checkbox" name="' + field_set_option + '" value="editable=False" id="id_' + field_set_option + '_3" /> editable</label></li><li><label for="id_' + field_set_option + '_4"><input type="checkbox" name="' + field_set_option + '" value="help_text=&quot;some help text for this field&quot;" id="id_' + field_set_option + '_4" /> help text</label></li><li><label for="id_' + field_set_option + '_5"><input type="checkbox" name="' + field_set_option + '" value="max_length=255" id="id_' + field_set_option + '_5" /> max length</label></li><li><label for="id_' + field_set_option + '_6"><input type="checkbox" name="' + field_set_option + '" value="null=True" id="id_' + field_set_option + '_6" /> null</label></li><li><label for="id_' + field_set_option + '_7"><input type="checkbox" name="' + field_set_option + '" value="related_name=&quot;some_special_name&quot;" id="id_' + field_set_option + '_7" /> related name</label></li><li><label for="id_' + field_set_option + '_8"><input type="checkbox" name="' + field_set_option + '" value="unique=False" id="id_' + field_set_option + '_8" /> unique</label></li><li><label for="id_' + field_set_option + '_9"><input type="checkbox" name="' + field_set_option + '" value="verbose_name=&quot;display name&quot;" id="id_' + field_set_option + '_9" /> verbose name</label></li></ul>';
                }
                $('#'+id_field_prefix + '_choice_list').replaceWith(field);
        };
})(jQuery);


