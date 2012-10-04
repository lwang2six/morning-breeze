FIELD_OPTION_BLANK = 'blank=True'
FIELD_OPTION_CHOICES = 'choices=[]'
FIELD_OPTION_DEFAULT = 'default=""'
FIELD_OPTION_EDITABLE = 'editable=False'
FIELD_OPTION_HELP_TEXT = 'help_text="some help text for this field"'
FIELD_OPTION_MAX_LENGTH = 'max_length=255'
FIELD_OPTION_NULL = 'null=True'
FIELD_OPTION_RELATED_NAME = 'related_name="some_special_name"'
FIELD_OPTION_UNIQUE = 'unique=False'
FIELD_OPTION_VERBOSE_NAME = 'verbose_name="display name"'

FIELD_OPTIONS_DEFAULT = (
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
FIELD_OPTIONS_DEFAULT_SET = set([FIELD_OPTION_BLANK, FIELD_OPTION_CHOICES, FIELD_OPTION_DEFAULT,
                                 FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, 
                                 FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, 
                                 FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE,
                                 FIELD_OPTION_VERBOSE_NAME])

FIELD_OPTIONS_BOOL = (
    ('default=False' , 'default'),
    (FIELD_OPTION_EDITABLE, 'editable'), 
    (FIELD_OPTION_HELP_TEXT, 'help text'),
    (FIELD_OPTION_RELATED_NAME, 'related name'), 
    (FIELD_OPTION_VERBOSE_NAME, 'verbose name'), 
)
FIELD_OPTIONS_BOOL_SET = set(['default=False', FIELD_OPTION_EDITABLE, FIELD_OPTION_DEFAULT,
                              FIELD_OPTION_HELP_TEXT, FIELD_OPTION_RELATED_NAME,
                              FIELD_OPTION_VERBOSE_NAME])

FIELD_OPTIONS_CHAR = FIELD_OPTIONS_DEFAULT
FIELD_OPTIONS_CHAR_SET = FIELD_OPTIONS_DEFAULT_SET

FIELD_OPTIONS_DATETIME = (
    (FIELD_OPTION_BLANK , 'blank'),
    ('default=datetime.datetime.now' , 'default'),
    (FIELD_OPTION_EDITABLE, 'editable'), 
    (FIELD_OPTION_HELP_TEXT, 'help text'),
    (FIELD_OPTION_NULL, 'null'), 
    (FIELD_OPTION_RELATED_NAME, 'related name'), 
    (FIELD_OPTION_VERBOSE_NAME, 'verbose name'), 
)
FIELD_OPTIONS_DATETIME_SET = set([FIELD_OPTION_BLANK, 'default=datetime.datetime.now',FIELD_OPTION_DEFAULT,
                                  FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, 
                                  FIELD_OPTION_NULL, FIELD_OPTION_RELATED_NAME,
                                  FIELD_OPTION_VERBOSE_NAME])

FIELD_OPTIONS_FILE = (
    (FIELD_OPTION_BLANK , 'blank'),
    (FIELD_OPTION_DEFAULT , 'default'),
    (FIELD_OPTION_EDITABLE, 'editable'), 
    (FIELD_OPTION_HELP_TEXT, 'help text'),
    (FIELD_OPTION_MAX_LENGTH, 'max length'),
    (FIELD_OPTION_NULL, 'null'), 
    (FIELD_OPTION_RELATED_NAME, 'related name'), 
    (FIELD_OPTION_UNIQUE, 'unique'),
    (FIELD_OPTION_VERBOSE_NAME, 'verbose name'), 
)
FIELD_OPTIONS_FILE_SET = set([FIELD_OPTION_BLANK, FIELD_OPTION_DEFAULT,
                              FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, 
                              FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, 
                              FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE,
                              FIELD_OPTION_VERBOSE_NAME])

FIELD_OPTIONS_FK = (
    (FIELD_OPTION_BLANK , 'blank'),
    (FIELD_OPTION_EDITABLE, 'editable'), 
    (FIELD_OPTION_HELP_TEXT, 'help text'),
    (FIELD_OPTION_NULL, 'null'), 
    (FIELD_OPTION_RELATED_NAME, 'related name'), 
    (FIELD_OPTION_VERBOSE_NAME, 'verbose name'), 
)
FIELD_OPTIONS_FK_SET = set([FIELD_OPTION_BLANK, FIELD_OPTION_EDITABLE,
                            FIELD_OPTION_HELP_TEXT, FIELD_OPTION_NULL, 
                            FIELD_OPTION_RELATED_NAME, FIELD_OPTION_VERBOSE_NAME])

FIELD_OPTIONS_IMAGE = FIELD_OPTIONS_FILE
FIELD_OPTIONS_IMAGE_SET = FIELD_OPTIONS_FILE_SET

FIELD_OPTIONS_INTEGER = (
    (FIELD_OPTION_BLANK , 'blank'),
    ('default=0' , 'default'),
    (FIELD_OPTION_EDITABLE, 'editable'), 
    (FIELD_OPTION_HELP_TEXT, 'help text'),
    (FIELD_OPTION_MAX_LENGTH, 'max length'),
    (FIELD_OPTION_NULL, 'null'), 
    (FIELD_OPTION_RELATED_NAME, 'related name'), 
    (FIELD_OPTION_UNIQUE, 'unique'),
    (FIELD_OPTION_VERBOSE_NAME, 'verbose name'), 
)
FIELD_OPTIONS_INTEGER_SET = set([FIELD_OPTION_BLANK, 'default=0', FIELD_OPTION_DEFAULT,
                                 FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, 
                                 FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, 
                                 FIELD_OPTION_RELATED_NAME, FIELD_OPTION_UNIQUE,
                                 FIELD_OPTION_VERBOSE_NAME])

FIELD_OPTIONS_PINT = FIELD_OPTIONS_INTEGER
FIELD_OPTIONS_PINT_SET = FIELD_OPTIONS_INTEGER_SET

FIELD_OPTIONS_TEXT = (
    (FIELD_OPTION_BLANK , 'blank'),
    (FIELD_OPTION_DEFAULT , 'default'),
    (FIELD_OPTION_EDITABLE, 'editable'), 
    (FIELD_OPTION_HELP_TEXT, 'help text'),
    (FIELD_OPTION_MAX_LENGTH, 'max length'),
    (FIELD_OPTION_NULL, 'null'), 
    (FIELD_OPTION_RELATED_NAME, 'related name'), 
    (FIELD_OPTION_VERBOSE_NAME, 'verbose name'), 
)
FIELD_OPTIONS_TEXT_SET = set([FIELD_OPTION_BLANK, FIELD_OPTION_DEFAULT,
                              FIELD_OPTION_EDITABLE, FIELD_OPTION_HELP_TEXT, 
                              FIELD_OPTION_MAX_LENGTH, FIELD_OPTION_NULL, 
                              FIELD_OPTION_RELATED_NAME,  FIELD_OPTION_VERBOSE_NAME])
