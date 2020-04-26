from . base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
	'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
	    'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/main_debug.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 7,
            #'formatter': 'main_formatter',
            'filters': ['require_debug_true'],
        },
	 	'null': {
            "class": 'logging.NullHandler',
        }
    },
    'loggers': {
        'aemapping': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'aenlu': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
		'aekm': {
			'handlers': ['console'],
			'level': 'DEBUG',
		},
		'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        '''py.warnings': {
            'handlers': ['null', ],
        },'''
        '': {
            'handlers': ['console', 'debug_file'],
            'level': "DEBUG",
		},
    }
}

