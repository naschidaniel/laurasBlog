#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The collection is needed for django commands."""

import logging
from invoke import task
from inv_base import manage_py
from inv_logging import success_logging


@task
def collectionstatic(c, **kwargs):
    """This function is used to collect the static files."""
    manage_py(c, "collectstatic -v 0 --no-input")
    success_logging(collectionstatic.__name__)


@task
def createsuperuser(c, **kwargs):
    """The function is used to create a superuser."""
    manage_py(c, "createsuperuser")
    success_logging(createsuperuser.__name__)


@task
def loadexampledata(c, **kwargs):
    """This function is used to load the sample data into the database."""
    manage_py(c, "loaddata db.json")
    success_logging(loadexampledata.__name__)


@task
def makemigrations(c, **kwargs):
    """This function is used to create magrations."""
    manage_py(c, "makemigrations")
    success_logging(makemigrations.__name__)


@task
def migrate(c, **kwargs):
    """This function is used to load migrations into the database."""
    manage_py(c, "migrate")
    success_logging(migrate.__name__)
