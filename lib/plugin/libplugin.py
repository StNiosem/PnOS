import os
import plugin
import plugin.libplugin

def RegisterPlugin(name: str, id: str, priority: int) : 
    #Name : Friendly Name for user (ex "Cool Plugin"); ID : plugin database name (ex "com.example.coolplugin"); Priority : important-ness level (0-999, 999=max)
    print("Registering PnPlugin : ", name)
