from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9e@k$(mnl!1feqdfa$9wl)2+)+ub63-aw5_k0)s()nuaerl)pq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'accounts',
    'toko',

    'ckeditor',
    'django_filters',
    'ckeditor_uploader',
    'numpy',
    # 'sweetify',
]

CKEDITOR_UPLOAD_PATH = 'uploads/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'crequest.middleware.CrequestMiddleware',
]

ROOT_URLCONF = 'myweb.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'myweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
   }
}

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql_psycopg2',
#          'NAME': 'db', 
#          'USER': 'postgres', 
#          'PASSWORD': 'admin123456',
#          'HOST': 'localhost', 
#          'PORT': '5432',
#      },

#       'users': {
#         'NAME': 'bln',
#         'ENGINE': 'django.db.backends.mysql',
#         'USER': 'root',
#         'HOST': 'localhost',
#         'PASSWORD': 'admin123456',
#         'PORT': '3306',
#     }

#  }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'db',
#         'USER': 'root',
#         'PASSWORD': 'admin123456',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# setting timzone indonesi



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# STATIC_ROOT = 'static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'anwarsanusi9412@gmail.com'
EMAIL_HOST_PASSWORD='idzizdrpbtblsert'



# CKEDITOR_CONFIGS = {
#    'default': {
#        'toolbar_Full': [
#             ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
#             ['Link', 'Unlink', 'Anchor'],
#             ['Image', 'Flash', 'Table', 'HorizontalRule'],
#             ['TextColor', 'BGColor'],
#             ['Smiley', 'SpecialChar'], ['Source'],
#             ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
#             ['NumberedList','BulletedList'],
#             ['Indent','Outdent'],
#             ['Maximize'],
#         ],
#         'extraPlugins': 'justify,liststyle,indent',
#    },
# }


# CKEDITOR_CONFIGS = {
#    'default': {
#         'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
#                 ['TextColor', 'BGColor'],
#                 ['Smiley', 'SpecialChar'],
#                 ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
#                  'JustifyRight', 'JustifyBlock'],
#                 ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'], ["Source"],
#                 ["Maximize"]],
#         'extraPlugins': 'justify,liststyle,indent',
#    },
# }





# STATIC_URL = '/static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# MEDIA_URL = '/media/'


# SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

