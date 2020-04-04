#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to test the functionality of DjangoVue before production."""

import os
import sys
import logging
from invoke import task
from inv_django import manage_py, makemigrations, migrate, collectionstatic
from inv_logging import inv_logging.success, inv_logging.task
from inv_node import npm, build
import inv_base
from inv_install import setenvironment
from inv_docker import start

@task
def starttest(c):
    """This function is used to start the production test environment."""
    inv_logging.task(starttest.__name__)
    static_folder = os.path.join(os.getcwd(), "django/static")
    try:
        shutil.rmtree(static_folder)
        logging.info(f"{static_folder} folder was deleted.")
    except:
        logging.error(f"{static_folder} could not be deleted.")

    setenvironment(c, "test")
    logging.info("The environment variables for production were set.")
    makemigrations(c)
    logging.info("The migrations were created.")
    migrate(c)
    logging.info("The database migrations were carried out.")
    collectionstatic(c)
    logging.info("The static files were stored in the static folder.")
    inv_base.docker_compose(c, f"up -d")
    setenvironment(c, "development")
    inv_logging.success(starttest.__name__)
