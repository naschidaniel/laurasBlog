#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""Basic functions for the fabric module."""

import logging
import os
import sys
import json


def read_settings(what):
    """A function to read the settings file."""
    settings_file = os.path.join(os.path.join(
        os.getcwd(), "fabric/settings.json"))
    if os.path.exists(settings_file):
        with open(settings_file) as f:
            settings = json.load(f)
    else:
        fabric_folder = os.path.join(os.path.join(os.getcwd(), "/fabric"))
        logging.error(
            f"There is no {settings_file} file available. Edit the settings.example.json file and rename the file in the {fabric_folder} folder to settings.json.")
        sys.exit(1)
    return settings[what]


def docker(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker"]
    command.append(cmd)
    command.insert(0, "export USERID=$UID && export GROUPID=$GID &&")
    logging.info(f"This command is executed: {command}")
    return c.run(" ".join(command), **kwargs)


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
