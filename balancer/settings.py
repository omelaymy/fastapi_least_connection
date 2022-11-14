import os
import configparser
from logging import INFO
from pathlib import Path


PROJECT_ROOT = Path(os.path.dirname(__file__)).parent

CONFIG_PATH = os.path.join(PROJECT_ROOT, 'balancer', 'config', 'config.ini')

CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)
REDIS_HOST = CONFIG['REDIS']['HOST']
REDIS_PORT = CONFIG['REDIS']['PORT']
AIOREDIS_URL = CONFIG['AIOREDIS']['URL']

SERVERS = CONFIG['INSTANCES']['ADDRESSES'].split(', ')

LOG_LEVEL = INFO
