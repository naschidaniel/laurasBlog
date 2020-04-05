#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The collection is needed for django commands."""

import logging
import os
import sys
from invoke import task, Collection
import inv_base
import inv_logging
import inv_docker

def manage_py(c, cmd, **kwargs):
    """The function is used to start a command inside a django container."""
    user, group = inv_base.uid_gid(c)
    inv_base.docker_compose(c, f"run -u {user}:{group} django python3 /www/site/manage.py {cmd}", pty=True)

@task
def collectstatic(c):
    """This function is used to collect the static files."""
    inv_logging.task(collectstatic.__name__)
    manage_py(c, "collectstatic -v 0 --no-input")
    inv_logging.success(collectstatic.__name__)


@task
def createsuperuser(c):
    """The function is used to create a superuser."""
    inv_logging.task(createsuperuser.__name__)
    logging.info("Enter the user for the Django backend.")
    inv_docker.stop(c)
    manage_py(c, "createsuperuser")
    inv_logging.success(createsuperuser.__name__)


@task
def loadexampledata(c):
    """This function is used to load the sample data into the database."""
    inv_logging.task(loadexampledata.__name__)
    manage_py(c, "loaddata db.json")
    inv_logging.success(loadexampledata.__name__)


@task
def managepy(c, cmd):
    """This function is used to create magrations."""
    inv_logging.task(managepy.__name__)
    manage_py(c, cmd)
    inv_logging.success(managepy.__name__)


@task
def makemigrations(c):
    """This function is used to create magrations."""
    inv_logging.task(makemigrations.__name__)
    manage_py(c, "makemigrations")
    inv_logging.success(makemigrations.__name__)


@task
def migrate(c):
    """This function is used to load migrations into the database."""
    inv_logging.task(migrate.__name__)
    inv_docker.stop(c)
    manage_py(c, "migrate")
    inv_logging.success(migrate.__name__)


@task
def generateSecretKey(c):
    """This function creates a new Secret Key for the fabric/settings.json file."""
    inv_logging.task(generateSecretKey.__name__)
    manage_py(c, "shell -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'")
    inv_logging.success(generateSecretKey.__name__)

django_ns = Collection("django")
django_ns.add_task(collectstatic)
django_ns.add_task(createsuperuser)
django_ns.add_task(generateSecretKey)
django_ns.add_task(loadexampledata)
django_ns.add_task(makemigrations)
django_ns.add_task(managepy)
django_ns.add_task(migrate)