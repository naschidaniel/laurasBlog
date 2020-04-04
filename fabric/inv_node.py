#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""The collection is needed for node."""

import os
import sys
import logging
from invoke import task, Collection
import inv_base
import inv_logging
import inv_django


@task
def build(c, **kwargs):
    """This function is used to build the Javascript components. The data is then integrated into django."""
    inv_logging.task(build.__name__)
    user, group = inv_base.uid_gid(c)
    inv_base.docker_compose(c, f"run -u {user}:{group} vue npm run build", pty=True)
    logging.info("The Vue components were built, minified and zipped.")
    inv_logging.success(build.__name__)


@task
def lint(c, **kwargs):
    """This command is used to embellish the code."""
    inv_logging.task(lint.__name__)
    user, group = inv_base.uid_gid(c)
    inv_base.docker_compose(c, f"run -u {user}:{group} vue npm run lint", pty=True)
    inv_logging.success(lint.__name__)


@task
def npm(c, cmd, **kwargs):
    """This function is used to respond to the packet manager npm."""
    inv_logging.task(npm.__name__)
    user, group = inv_base.uid_gid(c)
    inv_logging.cmd(cmd)
    inv_base.docker_compose(c, f"run -u {user}:{group} vue npm {cmd}", pty=True)
    inv_logging.success(npm.__name__)


node_ns = Collection("node")
node_ns.add_task(build)
node_ns.add_task(lint)
node_ns.add_task(npm)
