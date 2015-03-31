"""
Django settings for cs_web project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
import traceback


WS_TYPE = 'ws'


if sys.argv:

    try:

        for arg in sys.argv:

            print('sys argument :', arg)
            if arg == 'runsslserver':

                WS_TYPE = 'wss'


    except Exception:
        print('exception: ', sys.exc_info)
        traceback.print_exc()

# print('WS_TYPE: ', WS_TYPE)



import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))



DB_NAME = 'cs_web27'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'azi3$y2w^u1)qw4j!=rh=%q0h&5o_62f1cyi#+go((l#+kc#2f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ALLOWED_HOSTS = [
    'e-cab-27.cs.huji.ac.il',
    'e-10.cs.huji.ac.il',
]
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'ws4redis',

    "sslserver",

    'cs_web27',
    'cs_res27',
    'intercom',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cs_web27.urls'

WSGI_APPLICATION = 'cs_web27.wsgi.application'
# WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,            # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'cab-27',                # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)


SESSION_ENGINE = 'redis_sessions.session'

SESSION_REDIS_PREFIX = 'session'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'ws4redis.context_processors.default',
)



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


WEBSOCKET_URL = '/ws/'
WS4REDIS_EXPIRE = 7200
WS4REDIS_PREFIX = 'ws'
WS4REDIS_SUBSCRIBER = 'cs_web27.redis_store.RedisSubscriber'
WS4REDIS_HEARTBEAT = '--heartbeat--'




# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
print('STATIC_ROOT: ', STATIC_ROOT)


LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s %(module)s %(lineno)s] %(process)d %(thread)d %(message)s',
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '[%(levelname)s %(asctime)s] %(module)s %(lineno)s:  %(message)s',
            'datefmt' : "%H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'file.log'),
            'formatter': 'simple'
            },
        },
    'loggers': {

        'intercom': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },


        # '': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        #     },
        # This is useful for viewing DB queries
        # 'django': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        #     },
        }
    }

# if DEBUG:
#     # make all loggers use the console.
#     for logger in LOGGING['loggers']:
#         LOGGING['loggers'][logger]['handlers'] = ['console']