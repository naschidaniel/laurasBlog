#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to install DjangoVue."""

import os
import sys
import logging
from invoke import task
from inv_base import read_settings, manage_py
from inv_logging import success_logging, cmd_logging, task_logging
from inv_rsync import scp, ssh, rsync_push
from inv_build import rebuild, serve
from inv_node import npm
from inv_django import migrate, createsuperuser, loadexampledata


@task
def folders(c, cmd, **kwargs):
    """This function is used to start the production test environment."""
    task_logging(folders.__name__)
    cmd_logging(cmd)
    if cmd in ["development", "production"]:
        settings = read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter development or production.")
        sys.exit(1)

    for d in settings["initFolders"]:
        d = os.path.join(os.getcwd(), d)

        if not os.path.exists(d):
            try:
                os.makedirs(d)
                logging.info(f"The folder {d} has been created.")
            except:
                logging.error(f"The folder {d} could not be created.")
                sys.exit(1)
        else:
            logging.warning(f"The folder {d} already exists.")

    success_logging(folders.__name__)


@task
def setenvironment(c, cmd):
    """The function writes the local environment variables for django and docker."""
    task_logging(setenvironment.__name__)
    cmd_logging(cmd)
    if cmd in ["development", "production", "test"]:
        settings = read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter development or production.")
        sys.exit(1)

    if cmd in ["development", "test"]:
        development_dir = settings["docker"]["INSTALLFOLDER"]
        filename = ".env"
    else:
        development_dir = read_settings("development")
        development_dir = development_dir["docker"]["INSTALLFOLDER"]
        filename = ".env.production"

    dict_env = {
        "django": os.path.join(development_dir, f"django/djangoVue/{filename}"),
        "docker": os.path.join(development_dir, f"{filename}")
    }

    for dict_env_key, dict_env_value in dict_env.items():
        try:
            f = open(dict_env_value, "w")
            for key, value in settings[dict_env_key].items():
                f.write(f"{key}={value}\n")
                logging.info(
                    f"The environment variable {key} was written to the file '{dict_env_value}'.")
            f.close()
        except:
            logging.error(
                f"It was not possible to write to the file {dict_env_value}.")
            sys.exit(1)

    success_logging(setenvironment.__name__)
    return dict_env


@task
def quickinstallation(c):
    """A function for quick installation of djangoVue and start of a development server."""
    task_logging(quickinstallation.__name__)
    folders(c, "development")
    setenvironment(c, "development")
    rebuild(c)
    npm(c, "install")
    migrate(c)
    createsuperuser(c)
    loadexampledata(c)
    serve(c)
    success_logging(quickinstallation.__name__)


@task
def setproductionenvironment(c, cmd):
    """The function writes the environment variables on the server for django and docker. The created files are uploaded to the server and the required folders for djangoVue are created."""
    task_logging(setproductionenvironment.__name__)
    cmd_logging(cmd)
    if cmd == "production":
        settings = read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter production for the next steps.")
        sys.exit(1)

    dict_env = setenvironment(c, cmd)
    remote_env = {
        "django": os.path.join(settings["docker"]["INSTALLFOLDER"], "django/djangoVue/.env"),
        "docker": os.path.join(settings["docker"]["INSTALLFOLDER"], ".env")
    }

    scp(c, settings["remote_user"], settings["remote_host"],
        dict_env["docker"], remote_env["docker"])
    scp(c, settings["remote_user"], settings["remote_host"],
        dict_env["django"], remote_env["django"])

    os.system(f"rm {dict_env['docker']}")
    logging.info(
        f"The environment '{dict_env['docker']}' variable was deleted.")
    os.system(f"rm {dict_env['django']}")
    logging.info(
        f"The environment '{dict_env['django']}' variable was deleted.")

    for folder in settings['initFolders']:
        folder = os.path.join(settings["docker"]["INSTALLFOLDER"], folder)
        ssh(c, settings["remote_user"],
            settings["remote_host"], f"mkdir -p {folder}")

    success_logging(setproductionenvironment.__name__)
