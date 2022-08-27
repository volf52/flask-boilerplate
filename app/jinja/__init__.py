# -*- coding: utf-8 -*-
from flask import Flask

from app.jinja.context_processor import register_context_processor
from app.jinja.filters import register_filters


def register_jinja_mapping(app: "Flask"):
    register_filters(app)
    register_context_processor(app)
