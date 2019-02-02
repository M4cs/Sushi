import os
import sys

CUR_DIR = os.path.realpath(os.path.dirname(__file__))
DOWN_DIR = os.path.realpath(CUR_DIR + "/download/")
CONF_PATH = os.path.realpath(CUR_DIR + "/config/config.ini")
WIN_DOWN_LINK = 'https://github.com/s0uthwest/tsschecker/releases/download/330/tsschecker_win64_v330.zip'
MAC_DOWN_LINK = 'https://github.com/s0uthwest/tsschecker/releases/download/330/tsschecker_macOS_v330.zip'
LIN_DOWN_LINK = 'https://github.com/electimon/tsschecker/releases/download/330/tsschecker_linux_v330.zip'
PLATFORM = sys.platform

