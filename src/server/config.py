from configparser import ConfigParser
import os
import logging

from configargparse import argparse

APP_NAME = "AIDA"


def generate_config(options: argparse.Namespace):
    config = ConfigParser()
    config.add_section("config")
    for k, v in vars(options).items():
        if k == "generate_config":
            continue
        config.set("config", k, v)

    with open(options.config, "w") as conf:
        config.write(conf)


def get_default_data_folder() -> str:
    if os.name == "posix":  # Linux
        data_folder = os.getenv("XDG_DATA_HOME", os.path.expanduser(f"~/.local/share"))
        data_folder = os.path.join(data_folder, APP_NAME)
    elif os.name == "nt":  # Windows
        appdata = os.getenv("APPDATA")
        data_folder = os.path.join(appdata, APP_NAME)
    else:
        logging.warn("Unknown OS, defaulting to current working directory")
        data_folder = os.getcwd()  # Unsupported platform

    if not os.access(data_folder, os.W_OK | os.X_OK):
        logging.warn("No write permission, defaulting to current working directory")
        data_folder = os.getcwd()

    if data_folder is not None:
        os.makedirs(data_folder, exist_ok=True)

    return data_folder


def get_default_config_folder() -> str:
    if os.name == "posix":  # Linux
        config_folder = os.getenv("XDG_CONFIG_HOME", os.path.expanduser(f"~/.config/"))
        config_folder = os.path.join(config_folder, APP_NAME)
    elif os.name == "nt":  # Windows
        appdata = os.getenv("APPDATA")
        config_folder = os.path.join(appdata, APP_NAME)
    else:
        logging.warn("Unknown OS, defaulting to current working directory")
        config_folder = os.getcwd()  # Unsupported platform

    if not os.access(config_folder, os.W_OK | os.X_OK):
        logging.warn("No write permission, defaulting to current working directory")
        config_folder = os.getcwd()

    if config_folder:
        os.makedirs(config_folder, exist_ok=True)
    return config_folder
