#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import json
import os
import sys
import logging
import inv_install
import inv_local
import inv_test
from invoke import task, Collection, Program
from inv_logging import start_logging

# Logging
start_logging()

# Collections
MAIN_COLLECTION = Collection()

# Install Collection
INSTALL_NS = Collection("install")
MAIN_COLLECTION.add_collection(INSTALL_NS)
INSTALL_NS.configure({
    "host": "local",
    "hostname": "local",
    "docker_compose_files": [
        "./docker-compose.test.yml"
    ]
})
INSTALL_NS.add_task(inv_install.folders)


# Testing Collection
TEST_NS = Collection("test")
MAIN_COLLECTION.add_collection(TEST_NS)
TEST_NS.configure({
    "host": "local",
    "hostname": "local",
    "docker_compose_files": [
        "./docker-compose.test.yml"
    ]
})
TEST_NS.add_task(inv_test.start)


# Local Collection
LOCAL_NS = Collection("local")
MAIN_COLLECTION.add_collection(LOCAL_NS)

LOCAL_NS.configure({
    "host": "local",
    "hostname": "local",
    "docker_compose_files": [
        "./docker-compose.dev.yml"
    ]
})

LOCAL_NS.add_task(inv_local.build)
LOCAL_NS.add_task(inv_local.serve)
LOCAL_NS.add_task(inv_local.npm)
LOCAL_NS.add_task(inv_local.rebuild)
LOCAL_NS.add_task(inv_local.run)


# Program
PROGRAM = Program(namespace=MAIN_COLLECTION)
PROGRAM.run()
