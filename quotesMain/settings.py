import os
import django_heroku
from decouple import config, Csv



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Apps
    'registration.apps.RegistrationConfig',
    'quotes.apps.QuotesConfig',
    'profiles.apps.ProfilesConfig',

    #SocialAuth
    'social_django',
    #CrispyForBootstrapSupport
    'crispy_forms',

    'django.contrib.postgres',

    # rest framework
    'rest_framework',
    'rest_framework.authtoken',
    # Django filters for rest api search fucntionality
    'django_filters',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

REST_FRAMEWORK={

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'PAGE_SIZE': 10
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #SocialAuth
    'social_django.middleware.SocialAuthExceptionMiddleware',
    #TimezoneMiddleware
    'quotes.middleware.TimezoneMiddleware',

]
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

AUTHENTICATION_BACKENDS = (

    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    #without Modelbackend normal user can not register
    'django.contrib.auth.backends.ModelBackend',
)



ROOT_URLCONF = 'quotesMain.urls'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL='home'
AUTH_USER_MODEL='registration.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #social auth
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect', 
                #Context_processor for quote Category
                'quotes.context_processors.add_quotesCategory_to_context',
                
            ],
        },
    },
]

SOCIAL_AUTH_FACEBOOK_KEY =config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET=config('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_TWITTER_KEY= config('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET= config('SOCIAL_AUTH_TWITTER_SECRET')
#SOCIAL_AUTH_FACEBOOK_SCOPE contains a list of permissions to access the data properties our application requires.
#  The email and user_link permissions request access to the user’s Facebook email and profile link respectively.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_TWITTER_SCOPE = ['email', 'user_link']

#SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS has a key — fields — 
# where the value is a list of attributes that should be returned by Facebook when the user has successfully logged in.
#  The values are dependent on SOCIAL_AUTH_FACEBOOK_SCOP .
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       
    'fields': 'id, name, email, picture.type(large), link'
    }
SOCIAL_AUTH_TWITTER_PROFILE_EXTRA_PARAMS = {       
    'fields': 'id, name, email, picture.type(large), link'
    }
#o store the data in the database, we need to specify them in SOCIAL_AUTH_FACEBOOK_EXTRA_DATA.
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
    ]
SOCIAL_AUTH_TWITTER_EXTRA_DATA = [                 
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
    ]

WSGI_APPLICATION = 'quotesMain.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER':config('DB_USER'),
        'PASSWORD':config('DB_PASSWORD'),
        'HOST':config('DB_HOST'),
        'PORT':5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# python manage.py collects the static files into static roots
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'quotesMain/static')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}
