#! /bin/env zsh

outputs($OUTPUTTYPE){
    lspci | grep -s "display"
}

register_driver($DRIVERNAME, $DRIVERTYPE, $DRIVERID){
    echo $DRIVERNAME,$DRIVERTYPE,$DRIVERID | tee "/sys/drivers/driversfile" 
    sysConfig reload
}