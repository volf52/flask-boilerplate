# -*- coding: utf-8 -*-
"""
https://flask.palletsprojects.com/en/2.2.x/templating/#context-processors
"""
from flask import Flask


def register_context_processor(app: "Flask"):
    @app.context_processor
    def inject_is_production():
        return dict(application_name="FlaskBoilerplate")
