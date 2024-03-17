# Libraries --- DON'T FORGET TO INCLUDE NETWORKlib in the OS build !!!!
import network
import os

# Variables
userDir = "~"

# Functions
def  CryptUserDir() :
    print("Encrypting User directory")
    os.DirEntry(userDir)
    
    if userDir == "" :
        print("UserDir path is empty. Cannot Continue")
        exit()

    