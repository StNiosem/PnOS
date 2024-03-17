#! /usr/bin/env bash

InitUSB(){ 
    tty /dev/tty3   
    echo "Initializing USB Driver"
    /usr/bin/env pnshell register_driver usb.load

}