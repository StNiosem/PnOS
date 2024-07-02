#! /usr/bin/env bash

InitUSB(){ 
    tty /dev/tty3   
    echo "Initializing USB Driver"
    /usr/bin/env pnshell --quit-once-complete register_driver usb.power 
    /usr/bin/env pnshell --bgexec-reportclosed boot_tracker -sysdriver='usb.power' 
}

InitUSB(--verbose)