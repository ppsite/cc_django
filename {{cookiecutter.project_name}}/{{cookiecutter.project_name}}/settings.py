"""
根据环境变量引入不同的配置文件
配置信息默认优先从 .env 文件中读取, 然后再读取环境变量
"""

from utils.env import Env

env = Env()

RUN_ENV = env.get('RUN_ENV', 'DEVELOP')

if RUN_ENV == 'DEVELOP':
    from config.develop import *
elif RUN_ENV == 'PRODUCT':
    from config.product import *
else:
    from config.develop import *
