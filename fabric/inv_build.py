
#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to test the functionality of DjangoVue before deployment."""

import os
import sys
from invoke import task
from inv_base import docker_compose, manage_py



@task
def run(c, cmd, **kwargs):
    """The function is used to start a command inside a django container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} {cmd}", pty=True)


@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "build")


@task
def serve(c):
    """This function is used to start the development environment."""
    docker_compose(c, f"up")


@task
def start(c):
    """ starts all docker containers """
    docker_compose(c, "up -d")


@task
def stop(c, which=None):
    if which is None:
        docker_compose(c, "down --remove-orphans")
    else:
        docker_compose(c, "stop {}".format(which))
