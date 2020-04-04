#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This function contains the most important docker commands."""

import logging
from invoke import task, Collection

import inv_base
import inv_logging
from inv_django import collectionstatic, makemigrations, migrate
from inv_node import build


@task
def docker(c, cmd):
    """Restart all docker containers."""
    inv_logging.task(restart.__name__)
    inv_logging.cmd(cmd)
    inv_base.dockerdaemon(c, cmd)
    inv_logging.success(restart.__name__)


@task
def restart(c):
    """Restart all docker containers."""
    inv_logging.task(restart.__name__)
    inv_base.docker_compose(c, "up -d --remove-orphans")
    inv_logging.success(restart.__name__)


@task
def fullrestart(c):
    """Restart all docker containers with force."""
    inv_logging.task(fullrestart.__name__)
    inv_base.docker_compose(c, "up -d --force-recreate")
    inv_logging.success(fullrestart.__name__)


@task
def run(c, cmd):
    """The function is used to start a command inside a django container."""
    inv_logging.task(run.__name__)
    user, group = inv_base.uid_gid(c)
    inv_logging.cmd(cmd)
    inv_base.docker_compose(c, f"run -u {user}:{group} {cmd}", pty=True)
    inv_logging.success(run.__name__)


@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    inv_logging.task(rebuild.__name__)
    inv_base.docker_compose(c, "build")
    inv_logging.success(rebuild.__name__)


@task
def rebuildhard(c):
    """Rebuild all containers with --no-cache."""
    inv_logging.task(rebuildhard.__name__)
    inv_base.docker_compose(c, "build --no-cache")
    fullrestart(c)
    inv_logging.success(rebuildhard.__name__)


@task
def serve(c):
    """This function is used to start the development environment."""
    inv_logging.task(serve.__name__)
    inv_base.docker_compose(c, "up")
    inv_logging.success(serve.__name__)


@task
def start(c):
    """This function is used to start all Docker Containers."""
    inv_logging.task(start.__name__)
    inv_base.docker_compose(c, "up -d")
    build(c)
    makemigrations(c)
    logging.info("The migrations were created.")
    migrate(c)
    logging.info("The database migrations were carried out.")
    collectionstatic(c)
    logging.info("The static files were stored in the static folder.")
    inv_logging.success(start.__name__)


@task
def stop(c):
    """This function is used to stop all Docker Containers."""
    inv_logging.task(stop.__name__)
    inv_base.docker_compose(c, "down --remove-orphans")
    inv_logging.success(stop.__name__)


@task
def logs(c, cmd):
    """This function is used to output Docker Container logs."""
    inv_logging.task(logs.__name__)
    inv_base.docker_compose(c, 'logs {}'.format(cmd))
    inv_logging.cmd(cmd)
    inv_logging.success(logs.__name__)

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