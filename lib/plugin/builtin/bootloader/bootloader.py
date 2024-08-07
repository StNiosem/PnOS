def bl_init(command: str, diskId: int, statusLogPath: str, logFileContents: str) : 
    # Command: {boot|list|repair}, diskId: Sata Port No. (0-999), statusLogPath: log file path (diskId/$PATH); can be empty, 
    # logFileContents: what to do if log file isn't empty {overwrite|add}  
    print("0x000001 BOOT SUCCESS")
    print("0x000002 BL-LD PYTHON SUCCESS")