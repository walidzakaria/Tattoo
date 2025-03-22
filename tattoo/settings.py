from pathlib import Path
import configparser
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = os.path.join(Path(BASE_DIR).parent.absolute(), 'frontend')
PARENT_DIR = Path(BASE_DIR).parent.absolute()


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.ini'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('App', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean('App', 'DEBUG')
LOCAL = config.getboolean('App', 'LOCAL')


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '104.219.248.96',
    'hanitattohurghada.com',
    'www.hanitattohurghada.com',
]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://104.219.248.96:8000',
    'http://104.219.248.96',
    'http://hanitattohurghada.com',
    'http://www.hanitattohurghada.com',
    'https://hanitattohurghada.com',
    'https://www.hanitattohurghada.com',
)

CSRF_TRUSTED_ORIGINS = [
    'http://104.219.248.96',
    'http://localhost',
    'http://127.0.0.1',
    'http://hanitattohurghada.com',
    'http://www.hanitattohurghada.com',
    'https://hanitattohurghada.com',
    'https://www.hanitattohurghada.com',
]

BASE_URL = 'https://hanitattohurghada.com'
SECURE_CROSS_ORIGIN_OPENER_POLICY = None


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_yasg',
    'explorer',
    
    'operation',
    'public',
]

MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tattoo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(FRONTEND_DIR, 'dist'),
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {  # Adding this section should work around the issue.
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

WSGI_APPLICATION = 'tattoo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config.get('Database', 'DB_ENGINE'),
            'NAME': config.get('Database', 'DB_NAME'),
            'USER': config.get('Database', 'DB_USER'),
            'PASSWORD': config.get('Database', 'DB_PASSWORD'),
            'HOST': config.get('Database', 'DB_HOST'),
            'PORT': config.get('Database', 'DB_PORT'),
            'OPTIONS': {
            'init_command': "SET SESSION sql_mode='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'",
            },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/


TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# Additional directories for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Global static files
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}


CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    'http://104.219.248.96',
    'http://104.219.248.96:8000',
    'http://hanitattohurghada.com',
    'http://www.hanitattohurghada.com',
    'https://hanitattohurghada.com',
    'https://www.hanitattohurghada.com',
]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config.get('Email', 'EMAIL_HOST')
EMAIL_HOST_USER = config.get('Email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('Email', 'EMAIL_HOST_PASSWORD')
EMAIL_PORT = config.get('Email', 'EMAIL_PORT')
# EMAIL_USE_TLS = config('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = config.get('Email', 'EMAIL_HOST_USER')
EMAIL_USE_SSL = True


CORS_ALLOW_ALL_ORIGINS = True

EXPLORER_CONNECTIONS = { 'Default': 'default' }
EXPLORER_DEFAULT_CONNECTION = 'default'
EXPLORER_PERMISSION_VIEW = lambda r: r.user.is_staff
EXPLORER_PERMISSION_CHANGE = lambda r: r.user.is_staff
EXPLORER_SQL_BLACKLIST = (
     # DML
    #  'COMMIT', 'MERGE', 'REPLACE', 'ROLLBACK', 'START', 'UPSERT', # 'DELETE', 'SET', 'UPDATE', 'INSERT',
    #  # DDL
    #  'ALTER', 'CREATE', 'DROP', 'RENAME', 'TRUNCATE',
    #  # DCL
    #  'GRANT', 'REVOKE',
 )


LANGUAGES = [
    ('en', 'English'),
    ('de', 'Deutsch'),
]
LANGUAGE_CODE = 'en'  # اللغة الافتراضية

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),  # Path to store translation files
]

ADMIN_EMAILS = config.get('App', 'ADMIN_EMAILS').split(';')
