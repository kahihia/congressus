"""
Django settings for congressus project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v!r#8-@k_be__nior8(nwst!s&s$51+qu+^^(04q3w!nd1v_u9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.flatpages',

    # 3rd party
    'crispy_forms',
    'admin_csv',
    'autoslug',
    'maintenancemode',
    'tinymce',

    # custom apps
    'adminmenu',
    'tickets',
    'events',
    'mywebsocket',
    'windows',
    'access',
    'dashboard',
    'invs',

    # 3rd party, here to override templates
    'extended_filters',
    'django_admin_listfilter_dropdown',
)

SITE_ID = 1

if os.path.exists(os.path.join(BASE_DIR, 'theme')):
    print("Custom theme found... Using it")
    INSTALLED_APPS = ('theme', ) + INSTALLED_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'middlewares.FixMaintenanceDup',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'congressus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.filesystem.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'congressus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (BASE_DIR + '/locale', )

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

CSRF_FAILURE_VIEW = 'tickets.views.csrf_failure'

INTERNAL_IPS = ['127.0.0.1']

# CUSTOM SETTINGS

ORDER_SIZE = 15
FROM_EMAIL = 'congressus@us.es'
SITE_URL = "http://localhost:8000"

# REDSYS TPV options
REDSYS_ENABLED = True
TPV_TERMINAL = 1
TPV_MERCHANT = 'XXXXXX'
TPV_URL = "https://sis-t.redsys.es:25443/sis/realizarPago"
# LANGS: Spanish - 001, English - 002
TPV_LANG = '002'
#TPV_URL = "https://sis.redsys.es/sis/realizarPago"
TPV_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TPV_MERCHANT_URL = SITE_URL + '/ticket/confirm/'

# PAYPAL
PAYPAL_ENABLED = False
PAYPAL_SANDBOX = True
PAYPAL_CLIENTID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
PAYPAL_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# STRIPE
STRIPE_ENABLED = False
STRIPE_PK = 'pk_live_xxxxxxxxxxxxxxxxxxxxxxxx'
STRIPE_SK = 'sk_live_xxxxxxxxxxxxxxxxxxxxxxxx'
STRIPE_NAME = 'No es magia es Wadobo S.L.L.'
STRIPE_DESC = ''
STRIPE_IMAGE = 'https://s3.amazonaws.com/stripe-uploads/acct_103f1h2csBUWpoVVmerchant-icon-713198-wadobo-icon.png'
STRIPE_BITCOIN = False

QRCODE = True
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
WS_SERVER = 'localhost:9007'
TIMESTEP_CHART = 'daily'
MAX_STEP_CHART = 10

INVITATION_ORDER_START = '01'
PRINT_FORMATS = ['A4', 'thermal', 'csv']

MAX_SEAT_BY_SESSION = 50
EXPIRED_SEAT_H = 5*60 # 5 minutes
EXPIRED_SEAT_C = 15*60 # 15 minutes
EXPIRED_SEAT_P = 35*60 # TPV expired: 35 minutes

ROW_RAND = 3

SHOW_TOOLBAR_CALLBACK = False

ACCESS_VALIDATE_INV_HOURS = True

try:
    from local_settings import *
except:
    print("NO LOCAL SETTINGS")

# Debug toolbar options
if DEBUG:
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar_line_profiler.panel.ProfilingPanel',
    ]

    INSTALLED_APPS = (
        'debug_toolbar',
        'debug_toolbar_line_profiler',
        'silk',
    ) + INSTALLED_APPS

    MIDDLEWARE_CLASSES = (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'silk.middleware.SilkyMiddleware',
    ) + MIDDLEWARE_CLASSES

    SILKY_PYTHON_PROFILER = True
    #SILKY_PYTHON_PROFILER_BINARY = True # crate file for view with snakeviz

    for tmpl in TEMPLATES:
        tmpl['OPTIONS']['context_processors'] = ['django.template.context_processors.debug'] + tmpl['OPTIONS']['context_processors']
