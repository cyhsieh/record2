from .settings import *
STATIC_ROOT = 'static'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWERDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False
