#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This function contains the most important docker commands."""

import os
import sys
import logging
import inv_base
from invoke import task, Collection
from inv_logging import task_logging, cmd_logging, success_logging
from inv_django import collectionstatic, makemigrations, migrate
from inv_node import build


@task
def docker(c, cmd):
    """Restart all docker containers."""
    task_logging(restart.__name__)
    cmd_logging(cmd)
    inv_base.dockerdaemon(c, cmd)
    success_logging(restart.__name__)


@task
def restart(c):
    """Restart all docker containers."""
    task_logging(restart.__name__)
    inv_base.docker_compose(c, "up -d --remove-orphans")
    success_logging(restart.__name__)


@task
def fullrestart(c):
    """Restart all docker containers with force."""
    task_logging(fullrestart.__name__)
    inv_base.docker_compose(c, "up -d --force-recreate")
    success_logging(fullrestart.__name__)


@task
def run(c, cmd):
    """The function is used to start a command inside a django container."""
    task_logging(run.__name__)
    uid = "{}:{}".format(os.getuid(), os.getgid())
    cmd_logging(cmd)
    inv_base.docker_compose(c, f"run -u {uid} {cmd}", pty=True)
    success_logging(run.__name__)


@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    task_logging(rebuild.__name__)
    inv_base.docker_compose(c, "build")
    success_logging(rebuild.__name__)


@task
def rebuildhard(c):
    """Rebuild all containers with --no-cache."""
    task_logging(rebuildhard.__name__)
    inv_base.docker_compose(c, "build --no-cache")
    fullrestart(c)
    success_logging(rebuildhard.__name__)


@task
def serve(c):
    """This function is used to start the development environment."""
    task_logging(serve.__name__)
    inv_base.docker_compose(c, "up")
    success_logging(serve.__name__)


@task
def start(c):
    """This function is used to start all Docker Containers."""
    task_logging(start.__name__)
    inv_base.docker_compose(c, "up -d")
    build(c)
    makemigrations(c)
    logging.info("The migrations were created.")
    migrate(c)
    logging.info("The database migrations were carried out.")
    collectionstatic(c)
    logging.info("The static files were stored in the static folder.")
    success_logging(start.__name__)


@task
def stop(c):
    """This function is used to stop all Docker Containers."""
    task_logging(stop.__name__)
    inv_base.docker_compose(c, "down --remove-orphans")
    success_logging(stop.__name__)


@task
def logs(c, cmd):
    """This function is used to output Docker Container logs."""
    task_logging(logs.__name__)
    inv_base.docker_compose(c, 'logs {}'.format(cmd))
    cmd_logging(cmd)
    success_logging(logs.__name__)

docker_compose_ns = Collection("docker-compose")
docker_compose_ns.add_task(restart)
docker_compose_ns.add_task(fullrestart)
docker_compose_ns.add_task(rebuildhard)
docker_compose_ns.add_task(rebuild)
docker_compose_ns.add_task(start)
docker_compose_ns.add_task(stop)
docker_compose_ns.add_task(serve)
docker_compose_ns.add_task(run)
docker_compose_ns.add_task(logs)