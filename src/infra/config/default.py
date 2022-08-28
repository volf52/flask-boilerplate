# -*- coding: utf-8 -*-
DEBUG = True

# https://flask-caching.readthedocs.io/en/latest/
CACHE_TYPE = "NullCache"

# override this value in instance/config.py
# flask-sentry configuration. sentry-sdk[flask]
SENTRY_ENABLED = False
SENTRY_DSN = ""

# *******************************************************************
# ****** AFTER THIS LINE YOU CAN DEFINE YOU OWN DEFAULT CONFIGURATIONS ******
# *******************************************************************
PORT = 8080
