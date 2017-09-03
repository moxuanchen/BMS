# -*- coding: utf-8 -*-

import os
import yaml


class Config(object):

    def __init__(self):
        yaml_file = os.path.join(os.path.dirname(__file__), self.__class__.__name__ + '.yaml')
        if os.path.exists(yaml_file):
            yaml_obj = yaml.load(open(yaml_file, 'r'))
            for key in yaml_obj.keys():
                self.__setattr__(key, yaml_obj[key])

    DEFAULT_USER_PWD = '111111'
    SECRET_KEY = "xxxxyadfadkfjaldjfalkdjfalkd"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:a1b2c3@A@localhost/bms?charset=utf8"


class ProdConfig(Config):
    DEBUG = False


def get_config_obj():
    env = os.environ.get('BMS_ENV', "dev")
    env_map = {
        'dev': DevConfig,
        "prod": ProdConfig
    }

    return env_map[env]()


if __name__ == "__main__":
    get_config_obj()
