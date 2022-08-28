# -*- coding: utf-8 -*-

from flask import Flask

# Blueprints
from src.web.blueprints.index.routes import blueprint as index_bp

BLUEPRINTS = [index_bp]


def register_blueprints(app: "Flask"):
    for bp in BLUEPRINTS:
        app.register_blueprint(bp)
