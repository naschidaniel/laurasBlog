#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to test the functionality of DjangoVue before deployment."""

import os
import sys
from invoke import task
from inv_base import docker_compose, manage_py
from inv_logging import task_logging, cmd_logging, success_logging


@task
def restart(c):
    """Restart all docker containers."""
    task_logging(restart.__name__)
    docker_compose(c, "up -d --remove-orphans")
    success_logging(restart.__name__)


@task
def fullrestart(c):
    """Restart all docker containers with force."""
    task_logging(fullrestart.__name__)
    docker_compose(c, "up -d --force-recreate")
    success_logging(fullrestart.__name__)


@task
def run(c, cmd, **kwargs):
    """The function is used to start a command inside a django container."""
    task_logging(run.__name__)
    uid = "{}:{}".format(os.getuid(), os.getgid())
    cmd_logging(cmd)
    docker_compose(c, f"run -u {uid} {cmd}", pty=True)
    success_logging(run.__name__)


@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    task_logging(rebuild.__name__)
    docker_compose(c, "build")
    success_logging(rebuild.__name__)


@task
def rebuildhard(c):
    """Rebuild all containers with --no-cache."""
    task_logging(rebuildhard.__name__)
    docker_compose(c, "build --no-cache")
    fullrestart(c)
    success_logging(rebuildhard.__name__)


@task
def serve(c):
    """This function is used to start the development environment."""
    task_logging(serve.__name__)
    docker_compose(c, f"up")
    success_logging(serve.__name__)


@task
def start(c):
    """This function is used to start all Docker Containers."""
    task_logging(start.__name__)
    docker_compose(c, "up -d")
    success_logging(start.__name__)


@task
def stop(c):
    """This function is used to stop all Docker Containers."""
    task_logging(stop.__name__)
    docker_compose(c, "down --remove-orphans")
    success_logging(stop.__name__)


@task
def logs(c, cmd):
    """This function is used to output Docker Container logs."""
    task_logging(logs.__name__)
    docker_compose(c, 'logs {}'.format(cmd))
    cmd_logging(cmd)
    success_logging(logs.__name__)
