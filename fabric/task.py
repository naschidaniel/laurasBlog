#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import json
import os
import sys
import logging
import inv_docker
import inv_django
import inv_install
import inv_node
import inv_test
import inv_rsync
from inv_logging import start_logging
from invoke import task, Collection, Program


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

    if what not in ["development", "test", "production"]:
        logging.error(
            f"No settings could be found in the file {settings_file} for your input: {what}")
        sys.exit(1)
    return settings[what]



# Logging
start_logging()

# Namespace
MAIN_NS = Collection()


# # Testing Collection
# test_ns = Collection("test")
# test_ns.configure(read_settings("test"))
# test_ns.add_task(inv_test.starttest)
# test_ns.add_task(inv_docker.docker_ns)
# MAIN_NS.add_collection(test_ns)

# Local Collection
local_ns = Collection("local")
local_ns.configure(read_settings("development"))
local_ns.add_task(inv_install.folders)

local_ns.add_task(inv_docker.docker)


local_ns.add_task(inv_install.setenvironment)
local_ns.add_task(inv_install.quickinstallation)
local_ns.add_collection(inv_docker.docker_compose_ns)
local_ns.add_task(inv_node.build)
local_ns.add_task(inv_node.npm)
local_ns.add_task(inv_node.lint)
local_ns.add_collection(inv_django.django_ns)

MAIN_NS.add_collection(local_ns)

# # Production Collection
# production_ns = Collection("production")
# production_ns.add_task(inv_rsync.push)
# production_ns.add_task(inv_install.setproductionenvironment)
# MAIN_NS.add_collection(production_ns)


# Program
PROGRAM = Program(namespace=MAIN_NS)
PROGRAM.run()
