# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, make_response, render_template

blueprint = Blueprint(
    "index", __name__, template_folder="templates", static_folder="static"
)


@blueprint.route("/", methods=["get"])
def index_route():
    return make_response(render_template("index.jinja2"))
