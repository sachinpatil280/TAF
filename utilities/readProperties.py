import configparser
import os

config = configparser.RawConfigParser()

# Get the directory of this script file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up one level to TAF directory and then to configurations
config_path = os.path.join(os.path.dirname(current_dir), 'configurations', 'config.ini')

config.read(config_path)


def read_config(config_section):
    values = dict(config.items(config_section))
    return values
