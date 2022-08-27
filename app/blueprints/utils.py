# -*- coding: utf-8 -*-
from typing import Callable, Optional

from app.utils import filesystem

IGNORE_FOLDERS = ["__pycache__", "__boilerplate__"]


LIST_BLUEPRINT_CB = Optional[Callable[[str], None]]


def list_blueprints(blueprints_folder, *, cb: LIST_BLUEPRINT_CB = None):
    available_blueprints = filesystem.list_dirs(
        blueprints_folder, ignore=IGNORE_FOLDERS
    )

    if cb:
        for blueprint_name in available_blueprints:
            cb(blueprint_name)

    return available_blueprints


def list_boilerplate_skeletons(boilerplate_folder):
    return filesystem.list_dirs(boilerplate_folder + "/skeletons")


def list_boilerplate_models(boilerplate_folder):
    return filesystem.list_files(boilerplate_folder + "/models", file_ext="py.template")
