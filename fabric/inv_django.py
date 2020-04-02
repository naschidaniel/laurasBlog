#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The collection is needed for django commands."""

import logging
from invoke import task, Collection
from inv_base import manage_py
from inv_logging import cmd_logging, success_logging, task_logging


@task
def collectionstatic(c, **kwargs):
    """This function is used to collect the static files."""
    task_logging(collectionstatic.__name__)
    manage_py(c, "collectstatic -v 0 --no-input")
    success_logging(collectionstatic.__name__)


@task
def createsuperuser(c, **kwargs):
    """The function is used to create a superuser."""
    task_logging(createsuperuser.__name__)
    logging.info("Enter the user for the Django backend.")
    manage_py(c, "createsuperuser")
    success_logging(createsuperuser.__name__)


@task
def loadexampledata(c, **kwargs):
    """This function is used to load the sample data into the database."""
    task_logging(loadexampledata.__name__)
    manage_py(c, "loaddata db.json")
    success_logging(loadexampledata.__name__)


@task
def managepy(c, cmd, **kwargs):
    """This function is used to create magrations."""
    task_logging(managepy.__name__)
    manage_py(c, cmd)
    success_logging(managepy.__name__)


@task
def makemigrations(c, **kwargs):
    """This function is used to create magrations."""
    task_logging(makemigrations.__name__)
    manage_py(c, "makemigrations")
    success_logging(makemigrations.__name__)


@task
def migrate(c, **kwargs):
    """This function is used to load migrations into the database."""
    task_logging(migrate.__name__)
    manage_py(c, "migrate")
    success_logging(migrate.__name__)


@task
def generateSecretKey(c, **kwargs):
    """This function creates a new Secret Key for the fabric/settings.json file."""
    task_logging(generateSecretKey.__name__)
    manage_py(c, "shell -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'")
    success_logging(generateSecretKey.__name__)

django_ns = Collection("django")
django_ns.add_task(collectionstatic)
django_ns.add_task(createsuperuser)
django_ns.add_task(generateSecretKey)
django_ns.add_task(loadexampledata)
django_ns.add_task(makemigrations)
django_ns.add_task(managepy)
django_ns.add_task(migrate)