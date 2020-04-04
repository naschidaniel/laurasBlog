#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to install DjangoVue."""

import os
import sys
import logging
from invoke import task, Collection
import inv_base
import inv_logging
import inv_docker
import inv_node
import inv_django
import inv_docker
import inv_rsync

@task
def quickinstallation(c):
    """A function for quick installation of djangoVue and start of a development server."""
    inv_logging.task(quickinstallation.__name__)
    folders(c, "development")
    setenvironment(c, "development")
    inv_docker.rebuild(c)
    inv_node.npm(c, "install")
    inv_django.migrate(c)
    inv_django.createsuperuser(c)
    inv_django.loadexampledata(c)
    inv_docker.serve(c)
    inv_logging.success(quickinstallation.__name__)


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

    inv_rsync.scp(c, settings["docker"]["REMOTE_USER"], settings["docker"]["REMOTE_HOST"],
        dict_env["docker"], remote_env["docker"])
    inv_rsync.scp(c, settings["docker"]["REMOTE_USER"], settings["docker"]["REMOTE_HOST"],
        dict_env["django"], remote_env["django"])

    os.system(f"rm {dict_env['docker']}")
    logging.info(
        f"The environment '{dict_env['docker']}' variable was deleted.")
    os.system(f"rm {dict_env['django']}")
    logging.info(
        f"The environment '{dict_env['django']}' variable was deleted.")

    for folder in settings['initFolders']:
        folder = os.path.join(settings["docker"]["INSTALLFOLDER"], folder)
        inv_rsync.ssh(c, settings["docker"]["REMOTE_USER"],
            settings["docker"]["REMOTE_HOST"], f"mkdir -p {folder}")

    inv_logging.success(setproductionenvironment.__name__)


install_ns = Collection("install")
install_ns.add_task(folders)
install_ns.add_task(setenvironment)
install_ns.add_task(setproductionenvironment)
install_ns.add_task(quickinstallation)
