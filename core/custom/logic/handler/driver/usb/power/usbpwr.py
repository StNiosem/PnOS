from pnos import module_detachable
from pnos import pnos
from pnos import bootloader

import load

import os

def usbpwr() :
    #REQUIRES USBLOAD TO BE 1
    print("USB PWR DRIVER")
    os.system("./usbpwrdriver.sh")