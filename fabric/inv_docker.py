#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This function contains the most important docker commands."""

import os
import sys
import logging
from invoke import task, Collection
from inv_logging import task_logging, cmd_logging, success_logging
from inv_django import collectionstatic, makemigrations, migrate
from inv_node import build


def uid_gid(c):
    """The USER and GROUP are generated using the function."""
    if c.config["collection"] == "production":
        user = c.config["docker"]["USER"]
        group = c.config["docker"]["GROUP"]
        logging.info(
            f"The command is executed for the following USER and GROUP: {user}:{group}")
    else:
        user = os.getuid()
        group = os.getgid()
    return user, group


def docker_environment(c, command):
    """The function generates the docker environment variables."""
    user, group = uid_gid(c)
    if c.config["collection"] == "production":
        command.insert(0, f"export USERID={user} && export GROUPID={group} &&")
    else:
        command.insert(0, f"export USERID={user} && export GROUPID={group} &&")
    return command


def dockerdaemon(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker"]
    command.append(cmd)
    logging.info(f"This command will be executed: {command}")
    return c.run(" ".join(command), **kwargs)


def docker_compose(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker-compose"]
    for config_file in c.docker_compose_files:
        command.append("-f")
        command.append(config_file)

    command.append(cmd)
    command = docker_environment(c, command)
    return c.run(" ".join(command), **kwargs)


@task
def docker(c, cmd):
    """Restart all docker containers."""
    task_logging(restart.__name__)
    cmd_logging(cmd)
    dockerdaemon(c, cmd)
    success_logging(restart.__name__)


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
def run(c, cmd):
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
    docker_compose(c, "up")
    success_logging(serve.__name__)


@task
def start(c):
    """This function is used to start all Docker Containers."""
    task_logging(start.__name__)
    docker_compose(c, "up -d")
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
    docker_compose(c, "down --remove-orphans")
    success_logging(stop.__name__)


@task
def logs(c, cmd):
    """This function is used to output Docker Container logs."""
    task_logging(logs.__name__)
    docker_compose(c, 'logs {}'.format(cmd))
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