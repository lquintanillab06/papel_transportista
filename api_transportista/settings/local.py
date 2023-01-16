from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '10.10.1.153','10.10.1.85','127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_config('DB_NAME'),
        'USER': get_config('USER'),
        'PASSWORD': get_config('PASSWORD'),
        'HOST': get_config('HOST'),
        'PORT': 3306 ,
        #'OPTIONS': {'ssl': False},
        'OPTIONS': {'ssl_mode': 'DISABLED'},
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f"{BASE_DIR}/templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
