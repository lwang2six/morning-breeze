

#from django.db import connections

#To ensure a temporary database gets created.
#try:
#    cursor = connections['default'].cursor()
#    cursor.execute('DROP DATABASE IF EXISTS scaffold_temp;')
#    cursor.execute('CREATE DATABASE scaffold_temp;')
SCAFFOLD_DATABASES = {
            'scaffold_temp':{
                    'ENGINE': 'django.db.backends.mysql', 
                    'NAME': 'n232', 
                    'USER': 'leo', 
                    'PASSWORD': '1234', 
                    'HOST': '', 
                    'PORT': '', 
            }}
#except:
#    print "issue with creating a temporary database, currently only support MySQL."
#    SCAFFOLD_DATABASES = {}

