import json
import sys
import os
import logging
import copy

def read_settings(what):
    """A function to read the settings file."""
    settings_file = os.path.join(os.path.join(
        os.getcwd(), "settings.json"))

    if what not in ["development", "test", "production"]:
        logging.error(
            f"No settings could be found in the file {settings_file} for your input: {what}")
        sys.exit(1)

    if os.path.exists(settings_file):
        with open(settings_file) as f:
            settings = json.load(f)
    else:
        fabric_folder = os.path.join(os.path.join(os.getcwd(), "/fabric"))
        logging.error(
            f"There is no {settings_file} file available. Edit the settings.example.json file in the {fabric_folder} folder and save it in the main folder.")
        sys.exit(1)

    if what == "test":
        settings["test"]["docker"]["INSTALLFOLDER"] = os.getcwd()
    return settings[what]


def uid_gid(c):
    if c.config["collection"] == "production":
        user = c.config["docker"]["USER"]
        group = c.config["docker"]["GROUP"]
    else:
        user = os.getuid()
        group = os.getgid()
    return user, group


def docker_environment(c, command):
    """The function generates the docker environment variables."""
    user, group = uid_gid(c)
    if c.config["collection"] == "production":
        command.insert(0, f"export USERID={user} && export GROUPID={group} &&")
    else:
        command.insert(0, f"export USERID={user} && export GROUPID={group} &&")
    return command


def dockerdaemon(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker"]
    command.append(cmd)
    logging.info(f"This command will be executed: {command}")
    return c.run(" ".join(command), **kwargs)


def docker_compose(c, cmd, **kwargs):
    """A function to start docker-compose."""
    command = ["docker-compose"]
    for config_file in c.docker_compose_files:
        command.append("-f")
        command.append(config_file)

    command.append(cmd)
    command = docker_environment(c, command)
    return c.run(" ".join(command), **kwargs)
