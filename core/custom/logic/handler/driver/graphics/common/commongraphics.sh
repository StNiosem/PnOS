#! /usr/bin/env bash

IntDriver(){ 
    tty /dev/tty3   
    echo "Initializing Common Graphics Adapter Driver"
    /usr/bin/env pnshell register_driver graphics
    /usr/bin/env pnshell outputs DISPLAY_ALL refresh

}