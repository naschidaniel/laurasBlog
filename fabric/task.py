#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import json
import os
import shutil
import sys
import logging
import inv_logging
from invoke import task, Collection, Program

# Logging
inv_logging.start_logging()

# Settings
def read_settings(what):
    """A function to read the settings file."""
    settings_file = os.path.join(os.path.join(os.getcwd(), "fabric/settings.json"))
    print(settings_file)
    if os.path.exists(settings_file):
        with open(settings_file) as f:
            settings = json.load(f)
        logging.info(f"The {settings_file} file was successfully read.")
    else:
        fabric_folder = os.path.join(os.path.join(os.getcwd(), "/fabric"))
        logging.error(f"There is no {settings_file} file available. Edit the settings.example.json file and rename the file in the {fabric_folder} folder to settings.json.")
        sys.exit(1)
    
    return settings[what]

# Rsync
#def rsync_push(c, local_dir, remote_dir, exclude=None):
    #"""A function to push data to the remote server."""
    #return _rsync(c, local_dir, remote_dir, exclude, push=True)


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
# Installation
@task
def folders(c, cmd, **kwargs):
    """This function is used to start the production test environment."""
    if cmd in ["development", "production"]:
        settings = read_settings(cmd)
    else:
        logging.error("Your entry was incorrect. Please enter development or production.")
        sys.exit(1)

    for f in settings["initFolders"]:
        f = os.path.join(os.getcwd(), f)
        
        if not os.path.exists(f):
            try:
                os.makedirs(f)
                logging.info(f"The folder {f} has been created.")
            except:
                logging.error(f"The folder {f} could not be created.")
                sys.exit(1)



# Testing
@task
def start(c):
    """This function is used to start the production test environment."""
    static_folder = os.path.join(os.getcwd(), "django/static")
    try:
        shutil.rmtree(static_folder)
        logging.info(f"{static_folder} folder was deleted.")
    except:
        logging.error(f"{static_folder} could not be deleted.")

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
def run(c, cmd, **kwargs):
    """The function is used to start a command inside a django container."""
    uid = "{}:{}".format(os.getuid(), os.getgid())
    return docker_compose(c, f"run -u {uid} {cmd}", pty=True)


MAIN_COLLECTION = Collection()

####### Init Collection
INIT_NS = Collection("init")
MAIN_COLLECTION.add_collection(INIT_NS)
INIT_NS.configure({
    "host": "local",
    "hostname": "local",
    "docker_compose_files": [
        "./docker-compose.test.yml"
    ]
})
INIT_NS.add_task(folders)



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

LOCAL_NS.add_task(build)
LOCAL_NS.add_task(serve)
LOCAL_NS.add_task(npm)
LOCAL_NS.add_task(rebuild)
LOCAL_NS.add_task(run)


####### Program
PROGRAM = Program(namespace=MAIN_COLLECTION)
PROGRAM.run()
