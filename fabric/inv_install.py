#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to install cigsanalysistool."""

import os
import sys
import logging
import shutil
from invoke import task, Collection
import inv_base
import inv_logging
import inv_docker
import inv_node
import inv_django
import inv_docker
import inv_rsync

@task
def check_upstream(c):
    """Check master """
    print("Do you really want to run on production? [y/N]")
    answer = input()

    if answer.upper() not in ("Y", "YES", "JA", "J"):
        sys.exit(1)

    if c.run("git rev-parse --abbrev-ref HEAD", hide=True).stdout.strip() != "master":
        logging.error("You are not in the master branch. Only the master branch can be uploaded onto the server.")
        sys.exit(1)

    c.run("git fetch origin master", hide=True)
    if c.run("git diff origin/master", hide=True).stdout.strip() != "":
        logging.error("Your local branch differs from upstream master (run git diff)")
        sys.exit(1)
    
    if c.run("git status --short", hide=True).stdout.strip() != "":
        logging.error("You have a dirty working directory (run git status)")
        sys.exit(1)
    
        
@task
def quickinstallation(c):
    """A task for quick installation of cigsanalysistool and start of a development server"""
    inv_logging.task(quickinstallation.__name__)
    folders(c)
    setenvironment(c, "development")
    inv_docker.rebuild(c)
    inv_node.npm(c, "install")
    inv_django.migrate(c)
    inv_django.createsuperuser(c)
    inv_django.loadexampledata(c)
    inv_node.build(c)
    inv_django.collectstatic(c)
    inv_docker.serve(c)
    inv_logging.success(quickinstallation.__name__)


@task
def getdockercert(c):
    """A task to store the batch of docker certificates under ./fabric/cert"""
    inv_logging.task(getdockercert.__name__)
    settings = inv_base.read_settings("production")
    cert_path = settings["docker"]["DOCKER_CERT_PATH"]
    logging.info(f"The following path is used to store the certificates: {cert_path}")
    if os.path.exists(cert_path):
        shutil.rmtree(cert_path)
        logging.info("The old certificates were deleted.")
    
    if not os.path.exists(cert_path):
        os.mkdir(cert_path)
        logging.info(f"The {cert_path} folder was created.")

    inv_rsync.scp_get(c, "", settings["REMOTE_HOST"], "~/.docker/*", cert_path)
    inv_logging.success(getdockercert.__name__)


@task
def folders(c):
    """This task is used to create the folder structure"""
    inv_logging.task(folders.__name__)
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
    """The task writes the local environment variables for django and docker, for example: development"""
    inv_logging.task(setenvironment.__name__)
    inv_logging.cmd(cmd)
    
    settings = inv_base.read_settings(cmd)
    development_dir = os.getcwd()
    if cmd == "production":
        filename = ".env.production"
    else:
        filename = ".env"

    dict_env = {
        "django": os.path.join(development_dir, f"django/djangoVue/{filename}"),
        "docker": os.path.join(development_dir, f"{filename}")
    }

    for dict_env_key, dict_env_file in dict_env.items():
        try:
            with open(dict_env_file, "w") as f:
                for key, value in settings[dict_env_key].items():                          
                    f.write(f"{key}={value}\n")
                f.close()
            logging.info(f"The environment variable for '{dict_env_key}'' from the settings.json file was successfully written to the .env file.: '{dict_env_file}'")

        except:
            logging.error(
                f"It was not possible to write to the file: '{dict_env_file}'")
            sys.exit(1)

    inv_logging.success(setenvironment.__name__)
    return dict_env


@task(pre=[check_upstream])
def setproductionenvironment(c):
    """The task writes the environment variables on the server for django and docker. The created files are uploaded to the server and the required folders for cigsanalysistool are created."""
    inv_logging.task(setproductionenvironment.__name__)
    settings = inv_base.read_settings("production")

    dict_env = setenvironment(c, "production")
    remote_env = {
        "django": os.path.join(settings["docker"]["INSTALLFOLDER"], "django/djangoVue/.env"),
        "docker": os.path.join(settings["docker"]["INSTALLFOLDER"], ".env")
    }

    inv_rsync.scp_push(c, settings["REMOTE_USER"], settings["REMOTE_HOST"],
        dict_env["docker"], remote_env["docker"])
    inv_rsync.scp_push(c, settings["REMOTE_USER"], settings["REMOTE_HOST"],
        dict_env["django"], remote_env["django"])

    os.system(f"rm {dict_env['docker']}")
    logging.info(
        f"The environment '{dict_env['docker']}' variable was deleted.")
    os.system(f"rm {dict_env['django']}")
    logging.info(
        f"The environment '{dict_env['django']}' variable was deleted.")

    for folder in settings['initFolders']:
        folder = os.path.join(settings["docker"]["INSTALLFOLDER"], folder)
        inv_rsync.ssh(c, settings["REMOTE_USER"],
            settings["REMOTE_HOST"], f"mkdir -p {folder}")

    inv_logging.success(setproductionenvironment.__name__)

@task(pre=[check_upstream])
def deploy(c):
    """Everything you need to deploy"""
    inv_logging.task(deploy.__name__)
    c.run("./task.py local.node.build")
    c.run("./task.py local.django.collectstatic")
    inv_docker.stop(c)
    inv_rsync.push(c)
    setproductionenvironment(c)
    inv_docker.rebuild(c)
    inv_django.migrate(c)
    inv_docker.start(c)
    inv_logging.success(deploy.__name__)


install_ns = Collection("install")
install_ns.add_task(folders)
install_ns.add_task(getdockercert)
install_ns.add_task(setenvironment)
install_ns.add_task(quickinstallation)
