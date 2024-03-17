import pnos
from pnos import bootloader
import usbpower
import os

#USB LOAD
def usbload() :
    #PNOS Usb Loader
    print("PNOS usb loader, runs usbpwr scheduling task")
    os.system("./usbdriver.sh")