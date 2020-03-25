#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to install DjangoVue."""

import os
import sys
import logging
from invoke import task
from inv_base import read_settings, manage_py
from inv_logging import success_logging


@task
def folders(c, cmd, **kwargs):
    """This function is used to start the production test environment."""
    if cmd in ["development", "production"]:
        settings = read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter development or production.")
        sys.exit(1)

    for d in settings["initFolders"]:
        d = os.path.join(os.getcwd(), d)

        if not os.path.exists(d):
            try:
                os.makedirs(d)
                logging.info(f"The folder {d} has been created.")
            except:
                logging.error(f"The folder {d} could not be created.")
                sys.exit(1)
        else:
            logging.info(f"The folder {d} already exists.")

    success_logging(folders.__name__)


@task
def setenvironment(c, cmd, **kwargs):
    """The function writes the local enviroment variables for django and postgres."""
    if cmd in ["development", "production"]:
        settings = read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter development or production.")
        sys.exit(1)

    django_env = os.path.join(os.getcwd(), "django/.env")
    try:
        f = open(django_env, "w")
        for key, value in settings["django"].items():
            f.write(f"{key}={value}\n")
            logging.info(f"The enviroment variable {key} was written to the file '{django_env}'.")
        f.close()
    except:
        logging.error(f"TIt was not possible to write to the file {django_env}.")
        sys.exit(1)

    success_logging(folders.__name__)

