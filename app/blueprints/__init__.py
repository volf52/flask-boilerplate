# -*- coding: utf-8 -*-
from importlib import import_module

from flask import Flask

from app.blueprints.utils import list_blueprints


def register_blueprints(app: "Flask"):
    blueprint_dir = app.config.get("BLUEPRINTS_DIRECTORY")
    for blueprint_name in list_blueprints("app/blueprints"):
        blueprint_module = import_module("app.blueprints.%s.routes" % blueprint_name)

        app.register_blueprint(blueprint_module.blueprint)
