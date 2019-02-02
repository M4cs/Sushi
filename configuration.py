from configparser import ConfigParser
from utilities import getRealPath
from settings import *

def createConfig():
    config = ConfigParser()
    config['DEVICE'] = {
        'ecid': '',
        'model': '',
        'boardconfig': ''
    }
    
    with open(getRealPath(CUR_DIR + '/config/config.ini'), 'w') as f:
        config.write(f)
