from settings import *
import requests
import zipfile
import json
import subprocess

def getRealPath(oldpath):
    real_path = os.path.realpath(oldpath)
    return real_path

def downloadTSSChecker():
    if PLATFORM == 'win32' or PLATFORM == 'win64':
        name = '/tsschecker.exe'
        dl_url = WIN_DOWN_LINK
    elif PLATFORM == 'darwin':
        name = '/tsschecker'
        dl_url = MAC_DOWN_LINK
    r = requests.get(dl_url, allow_redirects=True)
    open(DOWN_DIR + '/tsschecker.zip', 'wb').write(r.content)
    zip_ref = zipfile.ZipFile(DOWN_DIR + '/tsschecker.zip', 'r')
    zip_ref.extractall(DOWN_DIR)
    zip_ref.close()
    os.remove(getRealPath(DOWN_DIR + '/tsschecker.zip'))
    if PLATFORM == 'darwin':
        os.chmod(getRealPath(DOWN_DIR + name), '+x')

def checkTSSChecker():
    if PLATFORM == 'win32' or PLATFORM == 'win64':
        name = '/tsschecker.exe'
    elif PLATFORM == 'darwin':
        name = '/tsschecker'
    if os.path.exists(getRealPath(DOWN_DIR + name)) == True:
        return True
    elif os.path.exists(getRealPath(DOWN_DIR + name)) == False:
        try:
            downloadTSSChecker()
            return True
        except:
            return False

def checkConfig():
    if os.path.exists(getRealPath(CUR_DIR + "/config/config.ini")) == False:
        return False
    else:
        return True

def getSignedFirmwares(identifier):
    headers = {'Accept':'application/json'}
    api = f'https://api.ipsw.me/v4/device/{identifier}?type=ipsw'
    r = requests.get(str(api), headers=headers).text
    obj = json.loads(r)
    signed = ''
    firmwares = obj['firmwares']
    numOfFirmwares = len(obj['firmwares'])
    for i in range(numOfFirmwares):
        if obj['firmwares'][i]['signed'] == True:
            if obj['firmwares'][i]['version'] not in signed:
                signed += '\n' + obj['firmwares'][i]['version']
    return signed

def saveBlobs(ecid, devId, boardconfig, version, latest):
    if PLATFORM == 'win32' or PLATFORM == 'win64':
        name = '/tsschecker.exe'
    elif PLATFORM == 'darwin':
        name = '/tsschecker'
    if version != '':
        query = [str(getRealPath(DOWN_DIR + name)),'-s','-i',version,'-e',ecid,'-d',devId,'-B',boardconfig]
    elif version == '':
        query = [str(getRealPath(DOWN_DIR + name)),'-s','-e',ecid,'-d',devId,'-B',boardconfig,latest]
    proc = subprocess.Popen(query, stdout=subprocess.PIPE, shell=True)
    out = proc.communicate()[0]
    return out.decode("utf-8")