import os
import sys
import libplugin as plugins
import bootloader

plugins.DeclarePlugin("self")
plugins.RegisterPlugin("PnOS Built-Ins", "sh.niosem.pnos.plugins.builtin", 999)

plugins.functions("filesystem", "os-probe", "packages", "config", "bootloader")

def bootloader() :
    print("Bootloader Config Utility")
    bootloader.bl_init("boot", 0, "0/log/bootloader/latest.log", "overwrite")