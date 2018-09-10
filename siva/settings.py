# -*- coding: utf-8 -*-
import os
import socket

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
ADMINS = ( ('Error Siva', ''),)
MANAGERS = ADMINS
servidor = socket.gethostname()

HOST_PRODUCCION = ''
HOST  = '127.0.0.1'
HOST_PRE_EXT = ''
HOST_DESARROLLO = ''


LANGUAGES = ('es','Spanish')
LANGUAGE_CODE = 'es-es'

DECIMAL_SEPARATOR=","
THOUSAND_SEPARATOR="."
TIME_ZONE = 'Atlantic/Canary'
TIME_INPUT_FORMATS = ('%I:%M %p', '%I:%M%p', '%H:%M:%S', '%H:%M')
TIME_FORMAT = 'h:i A'
DATE_FORMAT = "%d/%m/%Y"

SITE_ID  = 1
USE_I18N =False
USE_L10N =True
USE_TZ   =True #Coherencia en el almacenamiento de las fechas
ALLOWED_HOSTS = []


EMAIL_HOST = ''
EMAIL_HOST_PASSWORD =''
EMAIL_HOST_USER =''
EMAIL_PORT = 25
EMAIL_USE_TLS = 'True'
DEFAULT_FROM_EMAIL =''
SERVER_EMAIL =''

if servidor=='siva':
    BASE_URL_REPORTS   ="/reportes"
    #SERVER_URL_REPORTS ="""http://localhost:8080/jasperserver/flow.html?_flowId=viewReportFlow&reportUnit"""
    SERVER_URL_REPORTS = 'http://localhost:8080/jasperserver/services/repository?wsdl'
    USUARIO_JASPER     = ''
    PASSWD_JASPER      = ''
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    MEDIA_ROOT = PROJECT_ROOT+'/Documentos/'
    MEDIA_URL  = '/documentos/'
    HOST='127.0.0.1'
    URL_SERVER ="https://"
    URL_SER_REST = "http://"
    PRODUCCION = True
    USUARIO=''
    PASSWORD =''
    WSGI_APPLICATION = 'siva.wsgi.application'
    PATH_LOG= '/var/log/siva/'

elif servidor=='local':
    WSGI_APPLICATION = 'siva.wsgi.application'
    USUARIO_JASPER   = ''
    PASSWD_JASPER    = ''
    BASE_URL_REPORTS   ="/reportes"
    #SERVER_URL_REPORTS ="""http://siva.infinityloop.es:8080/jasperserver/flow.html?_flowId=viewReportFlow&reportUnit"""
    SERVER_URL_REPORTS = 'http://localhost:8080/jasperserver/services/repository?wsdl'
    DEBUG = True
    MEDIA_ROOT = PROJECT_ROOT+'/Documentos/'
    MEDIA_URL  = '/documentos/'
    URL_SERVER ="http://127.0.0.1:8000/"
    URL_SER_REST = URL_SERVER
    PRODUCCION = False
    USUARIO=''
    PASSWORD =''
    PATH_LOG= PROJECT_PATH



else:
    WSGI_APPLICATION = 'siva.wsgi.application'
    USUARIO_JASPER   = ''
    PASSWD_JASPER    = ''
    BASE_URL_REPORTS   ="/reportes"
    #SERVER_URL_REPORTS ="""http://siva.infinityloop.es:8080/jasperserver/flow.html?_flowId=viewReportFlow&reportUnit"""
    SERVER_URL_REPORTS = 'http://localhost:8080/jasperserver/services/repository?wsdl'
    DEBUG = False
    MEDIA_ROOT = PROJECT_ROOT+'/Documentos/'
    MEDIA_URL  = '/documentos/'
    URL_SERVER ="/"
    PRODUCCION = False
    USUARIO=''
    PASSWORD =''
    HOST = HOST_DESARROLLO
    PATH_LOG= '/var/log/siva/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'siva',                      # Or path to database file if using sqlite3.
        'USER': USUARIO,                      # Not used with sqlite3.
        'PASSWORD': PASSWORD,                  # Not used with sqlite3.
        #'HOST': HOST_DESARROLLO,
        'HOST': HOST,
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
	'OPTIONS': {'charset': 'utf8'},
    }
}



STATIC_ROOT = PROJECT_ROOT+'/static/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
STATICFILES_DIRS = (PROJECT_ROOT+"/media",)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
    'compressor.finders.CompressorFinder',
)


SECRET_KEY = '!r2uk)s3u#bu^9)ztywf^8)l89b1b5s$69v)78z^2#&amp;f7sz_l_'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

#Cache en produccion
# if DEBUG:
#     TEMPLATE_LOADERS +=  ('django.template.loaders.cached.Loader')


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    #'breadcrumbs.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', #cors
    'django.middleware.common.CommonMiddleware', #cors
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'context_processors.empresa.nombre_empresa',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages'
    )



ROOT_URLCONF = 'siva.urls'


TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'autocomplete_light',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'maestros_generales',
    'maestros',
    'reportes',
    'appcc',
    'clonar',
    'productos',
    'notificaciones.management.commands',
    'notificaciones',
    'trazabilidad',
    'dajaxice',
    'dajax',
    'selectable',
    'mptt',
    'crispy_forms',
    'floppyforms',
    'breadcrumbs',
    'private_files',
    'django_wysiwyg',
    'ckeditor',
    'loaddata',
    'rest_framework',
    'rest_framework_xml',
    'rest_framework.authtoken',
    'geoposition',
    'imagen',
    'landing_page',
    'gestion_usuarios',
    'compressor',
    'corsheaders',
    'djcelery',
    'rest_maestros',
   # 'rest_maestros_generales',
    'rest_loaddata',
    'rest_appcc',
    #'rest_waspmote',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
	    'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
	    'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': PATH_LOG+'django_console.log',
            'formatter': 'simple'
        },
        'development_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': PATH_LOG+'django_dev.log',
            'formatter': 'verbose'
        },
        'production_logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': PATH_LOG+'django_production.log',
            'formatter': 'simple'
        },
        'dba_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_false','require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': PATH_LOG+'django_dba.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'loaddata': {
            'handlers': ['console','development_logfile','production_logfile'],
            'propagate': True,
            'level': 'DEBUG',
         },
        'dba': {
            'handlers': ['console','dba_logfile'],
        },
        'django': {
            'handlers': ['console','development_logfile','production_logfile'],
        },
        'py.warnings': {
            'handlers': ['console','development_logfile'],
        },
    }
}

CORS_ORIGIN_ALLOW_ALL = True

GRAPPELLI_INDEX_DASHBOARD = 'siva.dashboard.CustomIndexDashboard'
if PRODUCCION:
    GRAPPELLI_ADMIN_TITLE="SIVA (SISTEMA INTEGRAL DE VIGILANCIA ALIMENTARIA)"
else:
    GRAPPELLI_ADMIN_TITLE="DESARROLLO"
    

#Configuracion Servidor de Reportes:
CRISPY_FAIL_SILENTLY = DEBUG
CRISPY_TEMPLATE_PACK = 'bootstrap'
CRISPY_CLASS_CONVERTERS = {'textinput': "textinput inputtext"}



SIVA_OPCION = (('MANTENIMIENTO','MANTENIMIENTO'),('POTABILIDAD_DEL_AGUA','POTABILIDAD AGUA'),('TEMPERATURAS','CONTROL TEMPERATURAS'),('RESIDUOS','CONTROL RESIDUOS'),('RELACION_FORMACION','FORMACION PERSONAL'),('RELACION_PROVEEDOR','HOMLOGACION PROVEEDORES'),('LIMPIEZA','PLAN LIMPIEZA'),('PLAGAS','CONTROL DE PLAGAS'))


#Control de sesion
SESSION_EXPIRE_AT_BROWSE_CLOSE = True
SESSION_COOKIE_AGE             = 3600
SESSION_SAVE_EVERY_REQUEST     = True


#DEFINICION DE TIPOS

ASESORSANITARIO="ASESOR SANITARIO" #PARAMETRIZA CONSULTAS

#DIAS DE MARGEN ANTE DE LANZAR EL AVISO DE NOTIFICACION
DIAS_NOTIFICACION=1



#Tipo de protección archivos estaticos
FILE_PROTECTION_METHOD = 'xsendfile'

CKEDITOR_UPLOAD_PATH = MEDIA_ROOT+"/uploads"

DJANGO_WYSIWYG_FLAVOR = 'yui'       # Default
DJANGO_WYSIWYG_FLAVOR = 'ckeditor'  # Requires you to also place the ckeditor files here:
DJANGO_WYSIWYG_MEDIA_URL = MEDIA_URL + "ckeditor/"


REST_FRAMEWORK = {
   'DEFAULT_PAGINATION_CLASS': 'siva.pagination.DstorePagination',
   'PAGE_SIZE': 25,
   'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.DjangoFilterBackend',
   ),
 "DEFAULT_RENDERER_CLASSES": (
        "rest_framework_json_api.renderers.JsonApiRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        'rest_framework_jsonp.renderers.JSONPRenderer',
        'rest_framework.renderers.AdminRenderer',
        # Any other renderers
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework_json_api.parsers.JsonApiParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
         #'rest_framework.authentication.TokenAuthentication',
         'rest_framework.permissions.IsAuthenticated',
         #'rest_framework.authentication.BasicAuthentication',
         #'rest_framework.authentication.SessionAuthentication',
          )
}

#CSRF_COOKIE_SECURE =False
#CSRF_COOKIE_NAME ='sivacsrftoken'

### COMPRESSION - django_compressor
COMPRESS_ENABLED = True
