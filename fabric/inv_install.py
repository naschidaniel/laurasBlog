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
            logging.warning(f"The folder {d} already exists.")

    success_logging(folders.__name__)


@task
def setenvironment(c, cmd, **kwargs):
    """The function writes the local environment variables for django and postgres."""
    if cmd in ["development", "production"]:
        settings = read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter development or production.")
        sys.exit(1)

    dict_env = {
        "django": os.path.join(os.getcwd(), "django/djangoVue/.env"),
        "postgres": os.path.join(os.getcwd(), ".env")
    }
    
    for dict_env_key, dict_env_value in dict_env.items():
        try:
            f = open(dict_env_value, "w")
            for key, value in settings[dict_env_key].items():
                f.write(f"{key}={value}\n")
                logging.info(f"The environment variable {key} was written to the file '{dict_env_value}'.")
            f.close()
        except:
            logging.error(f"It was not possible to write to the file {dict_env_value}.")
            sys.exit(1)

    success_logging(folders.__name__)
