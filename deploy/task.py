#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import os
import shutil
from invoke import task, Collection, Program


# rsync

def rsync_push(c, local_dir, remote_dir, exclude=None)
    return _rsync(c, local_dir, remote_dir, exclude, push=True)



# Docker

def docker_compose(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker-compose"]
    for config_file in c.docker_compose_files:
        command.append("-f")
        command.append(config_file)

    command.append(cmd)
    command.insert(0, "export USERID=$UID && export GROUPID=$GID &&")

    return c.run(" ".join(command), **kwargs)

def manage_py(c, cmd, **kwargs):
    """The function is used to start a command inside a django container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} django python3 /www/site/manage.py {cmd}", pty=True)



### Tasks



# Testing
@task
def start(c):
    """This function is used to start the production test environment."""
    static_folder = os.path.join(os.getcwd(), "django/static")
    shutil.rmtree(static_folder)
    print("{} Static Files Folder cleared".format(static_folder))
    
    manage_py(c, "migrate", pty=True)
    manage_py(c, "collectstatic --no-input", pty=True)
    docker_compose(c, f"up -d")


# Development
@task
def rebuild(c):
    """This function is used to recreate the docker containers."""
    docker_compose(c, "build")

@task
def npm(c, cmd, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} vue npm {cmd}", pty=True)

@task
def build(c, **kwargs):
    """This function is used to respond to the packet manager npm."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    docker_compose(c, f"run -u {uid} vue npm run build", pty=True)
    manage_py(c, "migrate")
    manage_py(c, "collectstatic -v 0 --no-input")

@task
def serve(c):
    """This function is used to start the development environment."""
    docker_compose(c, f"up")

@task
def djangoup(c, **kwargs):
    """The function is used to start a command inside a django container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} django", pty=True)


MAIN_COLLECTION = Collection()

####### Testing Collection
TEST_NS = Collection("test")
MAIN_COLLECTION.add_collection(TEST_NS)
TEST_NS.configure({
    "host": "local",
    "hostname": "local",
    "docker_compose_files": [
        "./docker-compose.test.yml"
    ]
})
TEST_NS.add_task(start)



####### Development Collection
LOCAL_NS = Collection("local")
MAIN_COLLECTION.add_collection(LOCAL_NS)

LOCAL_NS.configure({
    "host": "local",
    "hostname": "local",
    "docker_compose_files": [
        "./docker-compose.dev.yml"
    ]
})

LOCAL_NS.add_task(djangoup)
LOCAL_NS.add_task(serve)
LOCAL_NS.add_task(build)
LOCAL_NS.add_task(npm)
LOCAL_NS.add_task(rebuild)


####### Program
PROGRAM = Program(namespace=MAIN_COLLECTION)
PROGRAM.run()
