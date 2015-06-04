# To further or fully customize the paths, modify the following. Note that the
# default settings for each of these are relative to CONF_DIR and STORAGE_DIR
#
# Webapp config files

# Data directories
# NOTE: If any directory is unreadable in DATA_DIRS it will break metric browsing
# DATA_DIRS = [WHISPER_DIR, RRD_DIR] # Default: set from the above variables
#LOG_DIR = '/opt/graphite/storage/log/webapp'

import os
import string
from random import choice


def bool_env(name):
    val = os.environ.get(name, 'false')
    if 'f' in val.lower():
        return False
    elif 't' in val.lower():
        return True
    elif '0' in val:
        return False
    elif '1' in val:
        return True
    return False


GRAPHITE_ROOT = '/opt/graphite'
STORAGE_DIR = os.path.join(GRAPHITE_ROOT, 'storage')

LOG_DIR = os.path.join(STORAGE_DIR, 'logs')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "".join(choice(string.letters + string.digits) for _ in range(32))
)

MEMCACHE_HOSTS = ['127.0.0.1:11211']

WHISPER_DIR = os.path.join(STORAGE_DIR, 'whisper')
RRD_DIR = os.path.join(STORAGE_DIR, 'rrd')

DATABASES = {
    'default': {
        'NAME': os.path.join(STORAGE_DIR, 'graphite.db'),
        'ENGINE': 'django.db.backends.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

INDEX_FILE = os.path.join(STORAGE_DIR, 'index')
ALLOWED_HOSTS = ['*']

TIME_ZONE = os.environ.get('TZ', 'UTC')

LOG_RENDERING_PERFORMANCE = bool_env('LOG_RENDERING_PERFORMANCE')
LOG_CACHE_PERFORMANCE = bool_env('LOG_CACHE_PERFORMANCE')
LOG_METRIC_ACCESS = bool_env('LOG_METRIC_ACCESS')

DEBUG = bool_env("DEBUG")

DOCUMENTATION_URL = "http://graphite.readthedocs.org/"
DEFAULT_CACHE_DURATION = 60

CONF_DIR = os.path.join(GRAPHITE_ROOT, 'conf')
DASHBOARD_CONF = os.path.join(CONF_DIR, 'dashboard.conf')
GRAPHTEMPLATES_CONF = os.path.join(CONF_DIR, 'graphTemplates.conf')

# If using RRD files and rrdcached, set to the address or socket of the daemon
#FLUSHRRDCACHED = 'unix:/var/run/rrdcached.sock'

CONTENT_DIR = os.path.join(GRAPHITE_ROOT, 'webapp', 'content')
STATIC_ROOT = os.path.join(GRAPHITE_ROOT, 'static')
STATIC_URL = '/static/'
RRD_DIR = os.path.join(STORAGE_DIR, 'rrd')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
        }
    },
    'root': {
        'handlers': ['console', ],
        'level': os.environ.get('LOG_LEVEL', 'INFO')
    },
}
