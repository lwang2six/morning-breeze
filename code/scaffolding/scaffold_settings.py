#secondary database to be used to house data for scaffolding database operations.
SCAFFOLD_DATABASES = {
            'scaffold_temp':{
                    'ENGINE': 'django.db.backends.mysql', 
                    #please leave this unchanged
                    'NAME': 'scaffold_temp', 
                    #please change to a user that can create/modfiy database schemas
                    'USER': 'root',
                    #the password for that user
                    'PASSWORD': '1234', 
                    'HOST': '', 
                    'PORT': '', 
            }}

