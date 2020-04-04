
import os
import logging

def uid_gid(c):
    if c.config["collection"] == "production":
        user = os.getuid()
        group = os.getgid()
    else:
        user = c.config["docker"]["USER"]
        group = c.config["docker"]["GROUP"]
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
