import PySimpleGUIQt as p
from images import Images
import os
from settings import *
from configparser import ConfigParser
from utilities import getSignedFirmwares, saveBlobs, getRealPath
from configuration import createConfig
import webbrowser

p.SetOptions(background_color='#1e1e1e', element_background_color='#1e1e1e', text_color='#ffffff',
             input_elements_background_color='#111111', input_text_color='#636363',
             button_color=('#ffffff', '#3285f2'), border_width=0)

def mainScreen():
    if os.path.exists(CONF_PATH) == True:
        config = ConfigParser()
        config.read(CONF_PATH)
        model = config['DEVICE']['model']
        ecid = config['DEVICE']['ecid']
        boardconfig = config['DEVICE']['boardconfig']
        config_loaded = True
    else:
        model = 'None - Enter Device Identifier'
        ecid = 'None - Enter ECID'
        config_loaded = False
        boardconfig = 'None - Enter Boardconfig'
    version = '1.0.0~beta'
    col1 = [
        [p.T('Enter Device Identifier:', justification='center')],
        [p.Input(model, do_not_clear=True, key='_ID_')]
    ]
    col2 = [
        [p.T('Enter Board Config:', justification='center')],
        [p.Input(boardconfig, do_not_clear=True, key='_BOARDCONF_')]
    ]
    logo = [[p.Image(data_base64=Images.logo, click_submits=True, key='_LOGO_')]]
    title = [
        [p.T('Sushi | GUI Wrapper for TSSChecker', font=('Corbel', 15), text_color='#ffffff', justification='left')],
        [p.T('Sushi Version: ' + version, font=('Corbel', 10))],
        [p.T('Developed by @maxbridgland', click_submits=True, key='_TWITTER_')],
        [p.T('Licensed Under GNU GPLv3 | Made with Python')]
    ]
    layout = [
        [p.Column(logo), p.Column(title)],
        [p.HorizontalSeparator()],
        [p.T('Enter ECID:', justification='center')],
        [p.Input(ecid, do_not_clear=True, key='_ECID_', focus=True)],
        [p.Column(col1), p.VerticalSeparator(), p.Column(col2)],
        [p.T('iOS Version To Save:', justification='center'), p.Input('12.1.1', size=(10, 1), justification='center', key='_VER_'), p.Check('Save Latest Firmware', key='_LATEST_')],
        [p.HorizontalSeparator()],
        [p.Image(data_base64=Images.close_b, click_submits=True, key='Close'), p.Image(data_base64=Images.status_b, click_submits=True, key='Status'), p.Image(data_base64=Images.help_b, click_submits=True, key='Help'),
        p.Image(data_base64=Images.start_b, click_submits=True, key='Start')]
    ]
    window = p.Window('Sushi', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event == 'Close':
            exit()
            break
        elif event == 'Help':
            helpMenu()
        elif event == 'Status':
            statusMenu()
        elif event == 'Start':
            devId = values['_ID_']
            boardconfig = values['_BOARDCONF_']
            ecid = values['_ECID_']
            if values['_LATEST_'] == True:
                latest = ' -l '
                version = ''
            elif values['_LATEST_'] == False:
                latest = ''
                version = ' -i ' + values['_VER_']
            saveBlobs(ecid, devId, boardconfig, version, latest)
            finishedPopup(devId, ecid)
            if os.path.exists(CONF_PATH) == False:
                configMenu(ecid, devId, boardconfig)
        elif event == '_LOGO_':
            webbrowser.open_new_tab('https://github.com/M4cs/Sushi')
        elif event == '_TWITTER_':
            webbrowser.open_new_tab('https://twitter.com/maxbridgland')



def helpMenu():
    layout = [
        [p.T('Help Menu', font=('Corbel', 13), justification='left')],
        [p.T('''Status:
- Use the Status tool to check for signed firmwares.
- Press the Status button on the bottom.
- Enter Device Identifier [ex. iPhone8,1]
- Press Start and it will display available signed firmwares.

Saving Blobs:
- You only have to enter information the first time you save blobs.
- Enter ECID
- Enter Device Identifier
- Enter Boardconfig (You can obtain this from BMSSM)
- Enter Version You Would Like To Save Blobs For Or Check Latest iOS
- Press Start and Check Your Terminal For Output
- For some reason it seems to save blobs for all signed versions
automatically so either way you should be safe ¯\_(ツ)_/¯
    
Support:
- Either open up an Issue on GitHub (click the logo on the main screen)
or contact me on Twitter (@maxbridgland or click my name on the main screen).''')],
        [p.Image(data_base64=Images.close_b, click_submits=True, key='Close')]
    ]
    lol = p.Window('Sushi Help', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = lol.Read()
        if event == 'Close':
            break
    lol.Close()

def statusMenu():
    if os.path.exists(CONF_PATH) == True:
        config = ConfigParser()
        config.read(CONF_PATH)
        devId = config['DEVICE']['model']
    else:
        devId = ''
    layout = [
        [p.T('Enter Device Identifier [ex: iPhone8,1]: ')],
        [p.Input(devId, key='_DEVID_', do_not_clear=True)],
        [p.Image(data_base64=Images.close_b, click_submits=True, key='Close'), p.Image(data_base64=Images.start_b, click_submits=True, key='Start')]
    ]
    lmao = p.Window('Sushi Status', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = lmao.Read()
        if event == 'Start':
            devId = values['_DEVID_']
            signed = getSignedFirmwares(devId)
            p.Window('Signed Firmwares', keep_on_top=True, grab_anywhere=True, no_titlebar=True, auto_close=True, auto_close_duration=5).Layout(
                [[p.T('Signed Firmwares:' + signed, justification='center')]],
            ).Read()
        elif event == 'Close':
            break
    lmao.Close()

def configMenu(ecid, devId, boardconfig):
    layout = [
        [p.T('Would you like to save this configuration for the future?')],
        [p.Button('No'), p.Button('Yes')]
    ]
    window = p.Window('Save Screen', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event == 'No':
            break
        elif event == 'Yes':
            createConfig()
            config = ConfigParser()
            config.read(CONF_PATH)
            config['DEVICE']['ecid'] = ecid
            config['DEVICE']['model'] = devId
            config['DEVICE']['boardconfig'] = boardconfig
            with open(CONF_PATH, 'w') as f:
                config.write(f)
            break
    window.Close()    

def finishedPopup(devId, ecid):
    layout = [
        [p.T(f'Finished Saving Blobs For: {devId} with ECID: {ecid}\nCheck the downloads folder for your SHSH2 blobs!', justification='center')]
    ]
    window = p.Window('Finished', auto_close=True, keep_on_top=True, grab_anywhere=True, auto_close_duration=2, no_titlebar=True).Layout(layout).Read()
