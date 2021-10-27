# DEV SETTINGS

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

ENVIRONMENT = os.getenv("APPSETTING_WEBSITE_DEPLOY_TYPE")

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-100016333-2'

STATIC_URL = '/static/'

SITE_ID = 2

# Local logging configuration. This config applies only to
# the development environment. There is a unique logging config
# for each environment (e.g. staging, production).
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s,%(msecs)d %(levelname)-4s - [%(name)s] - [%(filename)s:%(lineno)d] %(message)s - [%(pathname)s]'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'django_file': {
            'level': 'WARNING',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': '/root/stonealgo/stonealgo/logging/django_file.log',
            'formatter': 'verbose'
        },
        'stonealgo_file': {
            'level': 'INFO',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': '/root/stonealgo/stonealgo/logging/stonealgo_file.log',
            'formatter': 'verbose'
        },
        'dashboard_file': {
            'level': 'INFO',
            # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': '/root/stonealgo/stonealgo/logging/dashboard_file.log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'CRITICAL',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'include_html': True,
        }
    },
    'loggers': {
        'main_app.stonealgo': {
            'handlers': ['stonealgo_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'dashboard.stonealgo': {
            'handlers': ['dashboard_file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['django_file', 'console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        }
    }
}

LOGGING_DIR = "./logging/"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*+3c^ymz%&#21hu7r-+l4)9o62m2_fl9(0_kve!%Cp)4cge*g25%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# For Debug Toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    '96.232.139.24',
    # ...
]

ADMINS = (
    ('Admin', 'management@stonealgo.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = "*"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mlrocks00',
        'HOST': 'stonealgo-dev.mysql.database.azure.com',
        'PORT': '3306',
        'USER': 'stonealgo@stonealgo-dev',
        'PASSWORD': 'ColdHarbor2018',
        'OPTIONS': {

        }
    }
}

SERVER_EMAIL = 'management@stonealgo.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'management@stonealgo.com'
EMAIL_HOST_PASSWORD = 'ColdHarbor18!'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'management@stonealgo.com'
THEME_CONTACT_EMAIL = 'management@stonealgo.com'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
SOCIALACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_ADAPTER = 'main_app.account_adapter.CustomAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'main_app.account_adapter.MySocialAccountAdapter'

ACCOUNT_USERNAME_REQUIRED = False

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    }
}

INTERNAL_USERS = [474, 449, 1101]

# Cookie name this can be whatever you want
SESSION_COOKIE_NAME = 'sessionid'  # use the sessionid in your views code

# the module to store sessions data
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# age of cookie in seconds (default: 2 weeks)
SESSION_COOKIE_AGE = 24 * 60 * 60 * 30

# whether a user's session cookie expires when the web browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# whether the session cookie should be secure (https:// only)
SESSION_COOKIE_SECURE = False

STRIPE_PUBLISHABLE_KEY = 'pk_test_kEEQs6mjTjszAED95qIljcMs00xT6gP8RY'
STRIPE_SECRET_KEY = 'sk_test_UOotGVCBfG6KtsZ2lssYs34t00DN1w0PLB'
STRIPE_TEST_SECRET_KEY = 'sk_test_UOotGVCBfG6KtsZ2lssYs34t00DN1w0PLB'
STRIPE_ENDPOINT_SECRET = 'whsec_EnDrscnouBsZXpLVqjZ1Nlp0enb8oPh3'

STRIPE_LIVE_MODE = False
DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # We don't use this, but it must be set
DJSTRIPE_FOREIGN_KEY_TO_FIELD = 'id'

sentry_sdk.init(
    dsn="https://27f0f9b8044d4d3ea882a1a091ba84fd@o932765.ingest.sentry.io/5902617",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)