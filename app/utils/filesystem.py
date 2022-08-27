# -*- coding: utf-8 -*-
import glob
import os
import pathlib
import shutil
from pathlib import Path
from string import Template

from genericpath import isfile


def create_folder_if_not(folder_path: os.PathLike):
    return os.makedirs(os.path.dirname(folder_path), exist_ok=True)


def list_files(
    directory, ignore: list[str] | None = None, file_ext: str | None = None
) -> list[str]:
    if ignore is None:
        to_ignore = {""}
    else:
        to_ignore = set(ignore)

    files: list[str] = []

    dir_path = Path(directory)
    for file in os.listdir(directory):
        if dir_path.joinpath(file).is_file():
            if file not in to_ignore:
                if file_ext and file.endswith(file_ext):
                    files.append(file)
                elif not file_ext:
                    files.append(file)

    return files


def list_dirs(directory, *, ignore: list[str] | None = None) -> list[str]:
    if ignore is None:
        to_ignore = {""}
    else:
        to_ignore = set(ignore)

    return list(
        filter(
            lambda x: os.path.isdir(os.path.join(directory, x)) and x not in to_ignore,
            os.listdir(directory),
        )
    )
