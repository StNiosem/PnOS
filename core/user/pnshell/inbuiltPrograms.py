import os
import subprocess
import sys

def register_driver(driverId: str, MBMemAllocation: int) :
    print("Registering driver: ", driverId, "with ", MBMemAllocation, "MB of memory (0 = auto)")