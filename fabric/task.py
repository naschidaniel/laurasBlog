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
from inv_base import read_settings
from invoke import task, Collection, Program

# Loggin
# start_logging()

# Namespace
MAIN_NS = Collection()


# # Testing Collection
# test_ns = Collection("test")
# test_ns.configure(inv_base.read_settings("test"))
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
