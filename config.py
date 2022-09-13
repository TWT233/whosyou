import os
from dataclasses import dataclass
from typing import Optional

import yaml


@dataclass
class _Config:
    bot_token: str
    db_url: str


_Config_: Optional[_Config] = None


def config() -> _Config:
    if not _Config_:
        load_config()
    return _Config_


def load_config():
    pwd = os.path.realpath(__file__)
    config_file = os.path.join(pwd, '../config.yaml')
    with open(config_file, 'r') as f:
        c = yaml.safe_load(f)
        global _Config_
        _Config_ = _Config(bot_token=c['bot']['token'], db_url=c['dal']['url'])
