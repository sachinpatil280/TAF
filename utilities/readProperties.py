import configparser
import os

config = configparser.RawConfigParser()

if "posix" in os.name:
    config.read("../configurations/config.ini")
else:
    config.read("..\\configurations\\config.ini")


def read_config(config_section):
    values = dict(config.items(config_section))
    return values
