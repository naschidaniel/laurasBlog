#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import os
from invoke import task, Collection, Program


def docker_compose(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker-compose"]
    for config_file in c.docker_compose_files:
        command.append("-f")
        command.append(config_file)

    command.append(cmd)
    command.insert(0, "export USERID=$UID && export GROUPID=$GID &&")

    return c.run(" ".join(command), **kwargs)

@task
def managepy(c, cmd, **kwargs):
    """The function is used to start a command inside a django container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} django python3 /www/site/manage.py {cmd}", pty=True)

@task
def npm(c, cmd, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} vue npm {cmd}", pty=True)

@task
def serve(c):
    """This function is used to start the development environment."""
    docker_compose(c, f"up")

@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "build")


MAIN_COLLECTION = Collection()

LOCAL_NS = Collection("local")
LOCAL_NS.configure({
    "host": "local",
    "hostname": "local",
    "docker_compose_files": [
        "./docker-compose.yml"
    ]
})
MAIN_COLLECTION.add_collection(LOCAL_NS)

LOCAL_NS.add_task(managepy)
LOCAL_NS.add_task(serve)
LOCAL_NS.add_task(npm)
LOCAL_NS.add_task(rebuild)

PROGRAM = Program(namespace=MAIN_COLLECTION)
PROGRAM.run()
