#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The fabricfile of the project."""

import json
import os
import sys
import logging
import inv_build
import inv_django
import inv_install
import inv_node
import inv_test
import inv_rsync
from inv_base import read_settings
from invoke import task, Collection, Program
from inv_logging import start_logging

# Logging
start_logging()

# Collections
MAIN_COLLECTION = Collection()

# Testing Collection
TEST_NS = Collection("test")
MAIN_COLLECTION.add_collection(TEST_NS)
TEST_NS.configure(read_settings("test"))
TEST_NS.add_task(inv_test.starttest)
TEST_NS.add_task(inv_build.stop)


# Local Collection
LOCAL_NS = Collection("local")
MAIN_COLLECTION.add_collection(LOCAL_NS)

LOCAL_NS.configure(read_settings("development"))

LOCAL_NS.add_task(inv_install.folders)
LOCAL_NS.add_task(inv_install.setenvironment)

LOCAL_NS.add_task(inv_build.restart)
LOCAL_NS.add_task(inv_build.fullrestart)
LOCAL_NS.add_task(inv_build.rebuildhard)
LOCAL_NS.add_task(inv_build.rebuild)
LOCAL_NS.add_task(inv_build.start)
LOCAL_NS.add_task(inv_build.stop)
LOCAL_NS.add_task(inv_build.serve)
LOCAL_NS.add_task(inv_build.run)
LOCAL_NS.add_task(inv_build.logs)

LOCAL_NS.add_task(inv_node.build)
LOCAL_NS.add_task(inv_node.npm)
LOCAL_NS.add_task(inv_node.lint)

LOCAL_NS.add_task(inv_django.collectionstatic)
LOCAL_NS.add_task(inv_django.createsuperuser)
LOCAL_NS.add_task(inv_django.generateSecretKey)
LOCAL_NS.add_task(inv_django.loadexampledata)
LOCAL_NS.add_task(inv_django.makemigrations)
LOCAL_NS.add_task(inv_django.managepy)
LOCAL_NS.add_task(inv_django.migrate)


# REMOTE Collection
REMOTE_NS = Collection("remote")
MAIN_COLLECTION.add_collection(REMOTE_NS)
REMOTE_NS.add_task(inv_rsync.push)
REMOTE_NS.add_task(inv_install.setproductionenvironment)


# Program
PROGRAM = Program(namespace=MAIN_COLLECTION)
PROGRAM.run()
