#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The collection is needed for node."""

import os
import sys
import logging
from invoke import task
from inv_base import docker_compose, manage_py
from inv_logging import success_logging, cmd_logging


@task
def npm(c, cmd, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    cmd_logging(cmd)
    docker_compose(c, f"run -u {uid} vue npm {cmd}", pty=True)
    success_logging(npm.__name__)


@task
def build(c, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} vue npm run build", pty=True)
    manage_py(c, "migrate")
    manage_py(c, "collectstatic -v 0 --no-input")
    success_logging(build.__name__)
