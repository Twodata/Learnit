"""
Django settings for twoanalytics project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
        'learnit.pythonanywhere.com',
        '127.0.0.1'
        ]    #  added 'learnit.pythonanywhere.com' for deployment purpose

# Email settings for PRODUCTION PURPOSE
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#SEND_GRID_API_KEY = ''
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = 'Twodata'
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Application definition

INSTALLED_APPS = [
    'Marketplace.apps.MarketplaceConfig',        
    'django.contrib.admin',    
    'registration', # add registration package    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notify',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'twoanalytics.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'twoanalytics.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         'ENGINE' : ENGINE,
         'NAME' : NAME,
         'USER' : USER,
         'PASSWORD' : PASSWORD,
         'HOST' : '127.0.0.1',
         'PORT' :'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


ADMINS = (
        ('Osabohien', 'osabohienchukwuma@gmail.com'),
        )   # added for deployment purposes

MANAGERS = ADMINS   # added for deployment purposes




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# django-registration-redux package variables
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 14
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/Marketplace/'
LOGIN_URL = '/accounts/login/'
SITE_ID = 1

DATE_INPUT_FORMAT = ['%d %B, %Y']



# Settings for django-notify
#NOTIFY_SOFT_DELETE = True
#NOTIFY_NF_LIST_CLASS_SELECTOR ='.notifications'
#NOTIFY_SINGLE_NF_CLASS_SELECTOR ='notifications'
#NOTIFY_NF_BOX_CLASS_SELECTOR ='.notification-box-list'
#NOTIFY_SINGLE_NF_BOX_CLASS_SELECTOR ='.notification-box'
#NOTIFY_MARK_NF_CLASS_SELECTOR ='.mark-notification'
#NOTIFY_MARK_ALL_NF_CLASS_SELECTOR ='.mark-all-notifications'
#NOTIFY_READ_NOTIFICATION_CSS ='read'
#NOTIFY_UNREAD_NOTIFICATION_CSS ='unread'
#NOTIFY_DELETE_NF_CLASS_SELECTOR ='.delete-notification'
#NOTIFY_UPDATE_TIME_INTERVAL = 1000


