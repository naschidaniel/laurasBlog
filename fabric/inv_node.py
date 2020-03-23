#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The collection is needed for node."""

import os
import sys
from invoke import task
from inv_base import docker_compose


@task
def npm(c, cmd, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} vue npm {cmd}", pty=True)
