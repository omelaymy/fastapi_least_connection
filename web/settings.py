import os
import configparser
from logging import INFO
from pathlib import Path


PROJECT_ROOT = Path(os.path.dirname(__file__)).parent
# APP_PATH = Path.dirname(__file__))
CONFIG_PATH = os.path.join(PROJECT_ROOT, 'web', 'config', 'config.ini')
CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_PATH)

REDIS_HOST = CONFIG['REDIS']['HOST']
REDIS_PORT = CONFIG['REDIS']['PORT']

SERVERS = CONFIG['INSTANCES']['ADDRESSES'].split(', ')

LOG_LEVEL = INFO

# REDIS_KEYS = list(
#         map(
#             lambda address: f"{address.split(' ')[-1]}",
#             INSTANCES_CONTAINER_NAMES
#         )
#     )
# print(REDIS_KEYS)
print(SERVERS)