# -*- coding: utf-8 -*-
# https://flask.palletsprojects.com/en/2.2.x/config/#builtin-configuration-values

DEBUG = True
IS_PRODUCTION = False

# https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.url_map
FLASK_STRICT_SLASHES = True

# https://flask-caching.readthedocs.io/en/latest/
CACHE_TYPE = "NullCache"

# override this value in instance/config.py
# flask-sentry configuration. sentry-sdk[flask]
SENTRY_ENABLED = False
SENTRY_DSN = ""


# *******************************************************************
# ****** AFTER THIS LINE YOU CAN DEFINE YOU OWN DEFAULT CONFIGURATIONS ******
# *******************************************************************
