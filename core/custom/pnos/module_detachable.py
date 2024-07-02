import os
import sys
import httplib2
import modulefinder

versionstring = "1.0.0"

def get_module() :
    print("getting detachable module for pnOS execution")
    if (httplib2.Http()) :
        print("Connection failed, cannot check for new version")
        return 2
    else :
        print("Checking for new version (current: ", versionstring, ")")
        if not (httplib2.Http()) :
            print("No new version found.")
            return 1
        else :
            print("new version available. downloading and installing")
            return 0