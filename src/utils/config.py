import configparser
import os

def get_config(config_file='config/settings.ini'):
    """Get configuration from settings.ini file"""
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        raise FileNotFoundError(f'The config file doesn\'t exist')
    

    config.read(config_file)
    return config
