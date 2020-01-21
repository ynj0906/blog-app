"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 以下Djangoシークレットキーの設定
SECRET_KEY = os.getenv('SECRET_KEY', None)



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["yastoon.com"]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contents.apps.ContentsConfig',#追加
    'django.forms',#追加
    'markdownx',#追加
    'django.contrib.sites',#django-allauth関係
    'allauth',#django-allauth関係
    'allauth.account',#django-allauth関係
    'allauth.socialaccount',#django-allauth関係
    'allauth.socialaccount.providers.github'#django-allauth関係
    

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

INTERNAL_IPS = ['127.0.0.1:8000']

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'contents.context_processors.common',#追加
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
  # 以下MySqlの設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME', None),
        'USER': os.getenv('USER', None),
        'PASSWORD': os.getenv('PASSWORD', None),
        'HOST': os.getenv('HOST', None),
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'charset': 'utf8',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO',

        }
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

#css/js/画像の配信用に追加
PROJECT_NAME = os.path.basename(BASE_DIR)

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)


#画像のアップロード用に追加
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/{}/media'.format(PROJECT_NAME)


MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.toc',
]

#ログイン/ログアウト時のリダイレクト用に追加
LOGIN_REDIRECT_URL = "/contents/main"
LOGOUT_REDIRECT_URL = "/contents/main"

#django-allauthの為に追加
ACCOUNT_LOGOUT_REDIRECT_URL="/accounts/login/"
# LOGIN_REDIRECT_URL = "/contents/main"
SITE_ID=1

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

###########
# Logging #
###########
#
# LOGGING = {
#     # バージョンは「1」固定
#     'version': 1,
#     # 既存のログ設定を無効化しない
#     'disable_existing_loggers': False,
#     # ログフォーマット
#     'formatters': {
#         # 本番用
#         'production': {
#             'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
#                       '%(pathname)s:%(lineno)d %(message)s'
#         },
#     },
#     # ハンドラ
#     'handlers': {
#         # ファイル出力用ハンドラ
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
#             'formatter': 'production',
#         },
#     },
#     # ロガー
#     'loggers': {
#         # 自作アプリケーション全般のログを拾うロガー
#         '': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         # Django本体が出すログ全般を拾うロガー
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#     },
# }

