"""CLI Controller for Divoom's Pixoo 64 by Taiga Tanaka"""
import command

import json

PIXOO64PROMPT = "PIXOO64: "
# print(command.httpRequest.__doc__)

# read the pixoo64.json file to enhance values into variables
with open('.\\conf\\pixoo64.json', 'r') as json_file:
    pixoo_info = json.load(json_file)

# Access variables from the loaded JSON data
HOSTNAME = pixoo_info['hostname']
DESCRIPTION = pixoo_info['description']
IPV4ADDR = pixoo_info['ipv4_address']
MACADDR = pixoo_info['mac_address']

# functionto iterate the result
def writeResults(result):
    """
    Prints the result on your terminal/CLI

    Parameters
    ----
    bool : boolean 
        returned value by command functions
    results : json 
        result retrieved by API requests
    """
    print("# <---------------------->")
    if result is None:
        return
    elif isinstance(result, bool):
        print(f"Command executed successfully: {result}")
    elif isinstance(result, dict):
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("Unexpected result type")

def showHelp(func):
    print("# <---------------------->")
    func.show_help()

def enum_command():
    print("# <---------------------->")
    pass

# writeResults(command.get_device_info(IPV4ADDR))
# writeResults(command.httpRequest(IPV4ADDR))
writeResults(command.getConfig.function(IPV4ADDR))
writeResults(command.getFaceID.function(IPV4ADDR))
writeResults(command.getDeviceTime.function(IPV4ADDR))
# showHelp(command.getDeviceTime)