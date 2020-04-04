#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to install DjangoVue."""

import os
import sys
import logging
import inv_base
from invoke import task
from inv_logging import inv_logging.success, inv_logging.cmd, inv_logging.task
from inv_rsync import scp, ssh, rsync_push
from inv_docker import rebuild, serve
from inv_node import npm
from inv_django import migrate, createsuperuser, loadexampledata


@task
def folders(c, cmd, **kwargs):
    """This function is used to start the production test environment."""
    inv_logging.task(folders.__name__)
    inv_logging.cmd(cmd)
    for d in c.config["initFolders"]:
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

    inv_logging.success(folders.__name__)


@task
def setenvironment(c, cmd):
    """The function writes the local environment variables for django and docker."""
    inv_logging.task(setenvironment.__name__)
    inv_logging.cmd(cmd)

    if cmd == "production":
        development_dir = inv_base.read_settings("development")
        development_dir = development_dir["docker"]["INSTALLFOLDER"]
        filename = ".env.production"
    else:
        development_dir = os.getcwd()
        filename = ".env"

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

    inv_logging.success(setenvironment.__name__)
    return dict_env


@task
def quickinstallation(c):
    """A function for quick installation of djangoVue and start of a development server."""
    inv_logging.task(quickinstallation.__name__)
    folders(c, "development")
    setenvironment(c, "development")
    rebuild(c)
    npm(c, "install")
    migrate(c)
    createsuperuser(c)
    loadexampledata(c)
    serve(c)
    inv_logging.success(quickinstallation.__name__)


@task
def setproductionenvironment(c, cmd):
    """The function writes the environment variables on the server for django and docker. The created files are uploaded to the server and the required folders for djangoVue are created."""
    inv_logging.task(setproductionenvironment.__name__)
    inv_logging.cmd(cmd)
    if cmd == "production":
        settings = inv_base.read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter production for the next steps.")
        sys.exit(1)

    dict_env = setenvironment(c, cmd)
    remote_env = {
        "django": os.path.join(settings["docker"]["INSTALLFOLDER"], "django/djangoVue/.env"),
        "docker": os.path.join(settings["docker"]["INSTALLFOLDER"], ".env")
    }

    scp(c, settings["docker"]["REMOTE_USER"], settings["docker"]["REMOTE_HOST"],
        dict_env["docker"], remote_env["docker"])
    scp(c, settings["docker"]["REMOTE_USER"], settings["docker"]["REMOTE_HOST"],
        dict_env["django"], remote_env["django"])

    os.system(f"rm {dict_env['docker']}")
    logging.info(
        f"The environment '{dict_env['docker']}' variable was deleted.")
    os.system(f"rm {dict_env['django']}")
    logging.info(
        f"The environment '{dict_env['django']}' variable was deleted.")

    for folder in settings['initFolders']:
        folder = os.path.join(settings["docker"]["INSTALLFOLDER"], folder)
        ssh(c, settings["docker"]["REMOTE_USER"],
            settings["docker"]["REMOTE_HOST"], f"mkdir -p {folder}")

    inv_logging.success(setproductionenvironment.__name__)
