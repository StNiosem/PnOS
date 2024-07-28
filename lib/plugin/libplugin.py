import os

def RegisterPlugin(name: str, id: str, priority: int) : 
    #Name : Friendly Name for user (ex "Cool Plugin"); ID : plugin database name (ex "com.example.coolplugin"); Priority : important-ness level (0-999, 999=max)
    print("-----| ", name, " |-----")
    print("Registering PnPlugin : ", name)
    print("ID : ", id)
    if (priority <= -1) :
        print("Priority too low, exiting.")
        exit(10)
    elif (-1 < priority < 334) :
        print("Priority : Low (", priority, ")")
    elif (333 < priority < 667) :
        print("Priority: Medium (", priority, ")")
    elif (666 < priority < 1000) :
        print("Priority: High (", priority, ")")
    elif (priority <= 1000) :
        print("Priority too high, exiting.")
        exit(11)

RegisterPlugin("nid", "migID", 1000)