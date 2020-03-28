#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to ensure data exchange between local PC and server."""

import os
import sys
import subprocess
import logging
from invoke import task
from inv_base import read_settings
from inv_logging import task_logging, success_logging, cmd_logging
from itertools import chain, repeat


def rsync_push(c, remote_user, remote_host, local_dir, remote_dir, exclude=None):
    return _rsync(c, remote_user, remote_host, local_dir, remote_dir, exclude, push=True)


def rsync_get(c, remote_user, remote_host, local_dir, remote_dir, exclude=None):
    return _rsync(c, remote_user, remote_host, local_dir, remote_dir, exclude, push=False)


def _rsync(c, remote_user, remote_host, local_dir, remote_dir, exclude=None, push=True):
    if exclude is None:
        exclude = []
    exclude_args = list(chain(*zip(repeat('--exclude'), exclude)))

    ssh_str = f"{remote_user}@{remote_host}:{remote_dir}"
    if push:
        cp = [local_dir, ssh_str]
    else:
        cp = [ssh_str, local_dir]

    rsync_cmd = ['rsync', '-a', '--delete-before'] + exclude_args + cp
    logging.info(f"The following rsync command is executed: {rsync_cmd}")
    subprocess.run(rsync_cmd, check=True)


@task
def push(c):
    task_logging(push.__name__)
    settings = read_settings("deployment")

    for rsync_task in settings["rsync"]:
        if "exclude" in settings["rsync"][rsync_task]:
            exclude = settings["rsync"][rsync_task]["exclude"]
        else:
            exclude = None
        
        logging.info(
            f"The settings {rsync_task} from the settings.json file are used for the deployment.")
        rsync_push(c, settings["remote_user"], settings["remote_host"], settings["rsync"][rsync_task]
                ["local_dir"], settings["rsync"][rsync_task]["remote_dir"], exclude)
    
    success_logging(push.__name__)
