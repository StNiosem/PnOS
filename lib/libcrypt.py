# Libraries --- DON'T FORGET TO INCLUDE NETWORKlib in the OS build !!!!
import network
import os
import hashlib
import base64

# Variables
userDir = "~"

# Functions
def DigestSha(undigested) :
    digested = undigested.HexDigest() 
    print(digested)
    return digested

def  CryptUserDir() :
    print("Encrypting User directory")
    os.DirEntry(userDir)
    
    if userDir == "" :
        print("UserDir path is empty. Cannot Continue")
        exit()
    
    

