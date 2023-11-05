#!Encoding:utf-8
# Pixoo64 controller commands 
"""Commands for controlling Pixoo64 by Divoom

Written by pf.tiger
"""
import requests
# import json
# import base64

FONT_LIST_URL = "https://app.divoom-gz.com/Device/GetTimeDialFontList"
IMG_UPLOAD_LIST_URL = "https://app.divoom-gz.com/Device/GetImgUploadList"
PIXOO64_URL = "http://10.0.0.61"
PIXOO64_IPV4 = "10.0.0.61"

BRIGHTNESS_MIN = 0
BRIGHTNESS_MAX = 100

COLORBALANCE_MIN = 0
COLORBALANCE_MAX = 100

class Command:
    """Treat pixoo64 commands as objects"""
    def __init__(self, name, description, function, type):
        self.name = name
        self.description = description
        self.function = function
        self.type = type

    def set_function(self, func):
        self.function = func
    
    def set_commandType(self, type):
        self.type = type

    def execute(self, *args, **kwargs):
        if self.function:
            return self.function(*args, **kwargs)
        else:
            print(f"No function set for the command '{self.name}'.")

    def show_help(self):
        print(f"Command: {self.name}")
        print(f"Type: {self.type}")
        print(self.function.__doc__)
        print("Usage: ")
        print(f"  {self.name} <arguments>")
        print("")

# Get
class Get_Command(Command):
    def __init__(self, name, description, function, type):
        super().__init__(name, description, function, "Get")

# Set
class Set_Command(Command):
    def __init__(self, name, description, function, type):
        super().__init__(name, description, function, "Set")

# Reset
class Reset_Command(Command):
    def __init__(self, name, description, function, type):
        super().__init__(name, description, function, "Reset")

# Bulk execution of the command given
def bulkExec():
    pass






# individual functions
def httpRequest(ipv4addr, port=80, command = "Channel/GetIndex", **kwargs):
    """
    function to send command via http.

    Parameters 
    ---
    ipv4addr : str
    port : int 
    command : str
    **kwargs : str

    Returns
    ----
    result : json
        parsed json data retrieved from pixoo64
    """

    url = f"http://{ipv4addr}:{port}/post"
    data = {"Command": command, **kwargs}
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        result = response.json()

        if "error_code" in result and result["error_code"] == 0:
            # Successful response, return parsed JSON
            return result
        else:
            print(f"Error: {result.get('error_code', 'Unknown error')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        return None

# return in text
def get_device_info(ipv4addr):
    """
    Gets the Pixoo64's device information. \n
    More at Divoom's official documentation:\n
    https://doc.divoom-gz.com/web/#/12?page_id=243

    Parameters
    ----
    ipv4addr : str
    
    """
    return httpRequest(ipv4addr, 80, "Channel/GetAllConf")

def get_faceId(ipv4addr):
    """
    Gets the Pixoo64's working Faces ID. \n
    More at Divoom's official documentation:\n
    https://doc.divoom-gz.com/web/#/12?page_id=239

    Parameters
    ----
    ipv4addr : str
    
    """
    return httpRequest(ipv4addr, 80, "Channel/GetClockInfo")

def get_deviceTime(ipv4addr):
    """
    Gets the Pixoo64's system time. \n
    More at Divoom's official documentation:\n
    https://doc.divoom-gz.com/web/#/12?page_id=337
    Parameters
    ----
    ipv4addr : str
    
    """
    return httpRequest(ipv4addr, 80, "Device/GetDeviceTime")


# create command objects
getConfig = Get_Command("Get-Config", get_device_info.__doc__, get_device_info, "Get")
getFaceID = Get_Command("Get-FaceID", get_faceId.__doc__, get_faceId, "Get")
getDeviceTime  = Get_Command("Get-DeviceTime", get_deviceTime.__doc__, get_deviceTime, "Get")
