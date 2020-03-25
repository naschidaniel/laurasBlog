#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to test the functionality of DjangoVue before deployment."""

import os
import sys
import logging
from invoke import task
from inv_base import docker_compose, manage_py


@task
def start(c):
    """This function is used to start the production test environment."""
    static_folder = os.path.join(os.getcwd(), "django/static")
    try:
        shutil.rmtree(static_folder)
        logging.info(f"{static_folder} folder was deleted.")
    except:
        logging.error(f"{static_folder} could not be deleted.")

    manage_py(c, "migrate", pty=True)
    manage_py(c, "collectstatic --no-input", pty=True)
    docker_compose(c, f"up -d")
