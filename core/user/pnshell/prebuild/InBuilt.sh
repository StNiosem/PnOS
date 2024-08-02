#! /bin/env zsh

outputs($OUTPUTTYPE){
    lspci | grep -s "$OUTPUTTYPE"
}

register_driver($DRIVERNAME, $DRIVERTYPE, $DRIVERID){
    echo "$DRIVERNAME,$DRIVERTYPE,$DRIVERID;" | tee "/sys/drivers/driversfile" 
    sysConfig reload
}

syscontrol($COMMAND){
    if $COMMAND == reboot 
        reboot
    fi
}