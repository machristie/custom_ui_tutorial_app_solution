"""
Override default Django settings for a particular instance.

Copy this file to settings_local.py and modify as appropriate. This file will
be imported into settings.py last of all so settings in this file override any
defaults specified in settings.py.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django - general settings
# Uncomment and specify for production deployments
# DEBUG = False
# STATIC_ROOT = "/var/www/path/to/sitename/static/"
# ALLOWED_HOSTS = ['production.hostname']

# Django - database settings
# MySQL - to use MySQL, uncomment and specify the settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '...',
#         'HOST': '...',
#         'USER': '...',
#         'PASSWORD': '...'
#     },
#     'OPTIONS': {
#         'init_command': 'SET default_storage_engine=INNODB,collation_connection=utf8_bin',
#     }
# }

# Django - Email settings
# Uncomment and specify the following for sending emails (default email backend
# just prints to the console)
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = '...'
# EMAIL_PORT = '...'
# EMAIL_HOST_USER = '...'
# EMAIL_HOST_PASSWORD = '...'
# EMAIL_USE_TLS = True
# ADMINS receive error emails
ADMINS = [('Admin Name', 'admin@example.com')]
# PORTAL_ADMINS receive administrative emails, like when a new user is created
# This can be set to a different value than ADMINS so that the PORTAL_ADMINS
# don't receive error emails
PORTAL_ADMINS = ADMINS
SERVER_EMAIL = 'portal@example.com'

# Keycloak Configuration
KEYCLOAK_CLIENT_ID = 'django-tutorial'
KEYCLOAK_CLIENT_SECRET = 'adaed995-feb8-4b10-a59d-2e5e4288ebfe'
KEYCLOAK_AUTHORIZE_URL = 'https://iam.scigap.org/auth/realms/default/protocol/openid-connect/auth'
KEYCLOAK_TOKEN_URL = 'https://iam.scigap.org/auth/realms/default/protocol/openid-connect/token'
KEYCLOAK_USERINFO_URL = 'https://iam.scigap.org/auth/realms/default/protocol/openid-connect/userinfo'
KEYCLOAK_LOGOUT_URL = 'https://iam.scigap.org/auth/realms/default/protocol/openid-connect/logout'
# Optional: specify if using self-signed certificate or certificate from unrecognized CA
# KEYCLOAK_CA_CERTFILE = os.path.join(BASE_DIR, "django_airavata", "resources", "incommon_rsa_server_ca.pem")
KEYCLOAK_VERIFY_SSL = True

AUTHENTICATION_OPTIONS = {
    # Control whether username/password authentication is allowed
    'password': {
        'name': 'Airavata Test Drive Gateway',
    },
    # Can have multiple external logins
    'external': [
        {
            'idp_alias': 'cilogon',
            'name': 'existing institution credentials',
            'logo': 'images/cilogon-logo-24x24-b.png',
        }
    ]
}

# Airavata API Configuration
GATEWAY_ID = 'default'
AIRAVATA_API_HOST = 'scigap02.sciencegateways.iu.edu'
AIRAVATA_API_PORT = 9930
AIRAVATA_API_SECURE = True
GATEWAY_DATA_STORE_RESOURCE_ID = 'gf4.ucs.indiana.edu_61552681-96f0-462a-a36c-a62a010bffc6'
GATEWAY_DATA_STORE_DIR = '/tmp/experiment-data-dir'
GATEWAY_DATA_STORE_HOSTNAME = 'gf4.ucs.indiana.edu'
GATEWAY_DATA_STORE_REMOTE_API = "https://testdrive.airavata.org/api"

# Profile Service Configuration
PROFILE_SERVICE_HOST = AIRAVATA_API_HOST
PROFILE_SERVICE_PORT = 8962
PROFILE_SERVICE_SECURE = False

# Sharing API Configuration
SHARING_API_HOST = AIRAVATA_API_HOST
SHARING_API_PORT = 7878
SHARING_API_SECURE = False

# Portal settings
PORTAL_TITLE = 'Airavata Test Drive Gateway'

# Logging configuration. Uncomment following to override default log configuration
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'formatters': {
#         'verbose': {
#             'format': '[%(asctime)s %(name)s:%(lineno)d %(levelname)s] %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'mail_admins': {
#             'filters': ['require_debug_false'],
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         }
#     },
#     'loggers': {
#         'django_airavata': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'DEBUG' if DEBUG else 'INFO'
#         },
#         'root': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'WARNING'
#         }
#     },
# }
