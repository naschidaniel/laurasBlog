#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
"""This collection is used to install DjangoVue."""

import os
import sys
import logging
from invoke import task
from inv_base import read_settings
from inv_logging import success_logging


@task
def folders(c, cmd, **kwargs):
    """This function is used to start the production test environment."""
    if cmd in ["development", "production"]:
        settings = read_settings(cmd)
    else:
        logging.error(
            "Your entry was incorrect. Please enter development or production.")
        sys.exit(1)

    for f in settings["initFolders"]:
        f = os.path.join(os.getcwd(), f)

        if not os.path.exists(f):
            try:
                os.makedirs(f)
                logging.info(f"The folder {f} has been created.")
            except:
                logging.error(f"The folder {f} could not be created.")
                sys.exit(1)
        else:
            logging.info(f"The folder {f} already exists.")
    
    success_logging(folders.__name__)
