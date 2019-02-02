from utilities import *
from settings import *
from screens import *
from configuration import *
from configparser import ConfigParser

def main():
    if checkTSSChecker() == True:
        pass
    elif checkTSSChecker() == False:
        print('Error: Something went wrong on startup.')
    mainScreen()
    
    

if __name__ == "__main__":
    main()