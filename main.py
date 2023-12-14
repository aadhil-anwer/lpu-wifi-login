import subprocess
import requests
import socket
import time
import re
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning from urllib3 needed for this script. (read about this dumbo.. chatgpt)
urllib3.disable_warnings(InsecureRequestWarning)
print("Loading Program:", end=" ")
for _ in range(8):
    print(".", end="", flush=True)
    time.sleep(0.1)
print(" \n")
def get_connected_ssid():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], universal_newlines=True)
        lines = result.split("\n")
        for line in lines:
            if "SSID" in line:
                return line.split(":")[1].strip()
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def check_ssid_presence(target_ssid):
    connected_ssid = get_connected_ssid()

    if connected_ssid is not None:
        print(f"Connected WIFI: {connected_ssid}")

        if target_ssid in connected_ssid:
            if "Jio" in connected_ssid:
                print("Not Official LPU, Its Jionet MF!")
                return False
                
            else:
                print(f"Good! Official LPU Stuff")
                return True;
                
        else:
            print(f"Connect to any of the LPU Wireless Network (LPU Wireless, LPU Hostel)")
            return False
            
    else:
        print(f"\nSomething Terribly wrong with Retrieving Your Connected WIFI.....\n Are yu even connected nigga?\n")
        #try to add wifi autoconnect feature here to connect to lpu wifi...(after completion)
        


ip = socket.gethostbyname(socket.gethostname())

def loggin_in():
    payload={'username':'12206717@lpu.com', 'password':'96148351', 'mode':'191', 'ipaddress':ip}
    r =requests.post('https://10.10.0.1/24online/servlet/E24onlineHTTPClient', verify=False, data=payload)
    r.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    
    res = r.text
    if "To start surfing" in res:
        print("Login successful")
    else:
        print("Login failed")



target_ssid = "LPU"  


# # if check_ssid_presence(target_ssid)==True:
# #     loggin_in()
# else:
#     print("Exiting Program")


def logging_out():
    payload={'username':'12206717@lpu.com', 'password':'96148351', 'mode':'193', 'ipaddress':ip, 'logintype':'2', 'loggedinuser':'12206717@lpu.com', 'logout':'Logout'}
    r =requests.post('https://10.10.0.1/24online/servlet/E24onlineHTTPClient', verify=False, data=payload)
    r.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    res = r.text
    if "To start surfing" in res:
        print("You have successfully logged off")
    else:
        print("Logout failed")

# def connect_to_wifi():
#     # subprocess.run(['netsh', 'interface', 'set', 'interface', 'Wi-Fi', 'admin=enabled'], shell=True)
#     available=subprocess.check_output(["netsh", "wlan" ,"show", "network"])
#     available=available.decode('UTF-8')
#     # print(available)
    
#     pattern=r"SSID \d+ : (.+)"
#     exclude=["Jio", "Guest"]
#     wifis=re.finditer(pattern, available)
#     valid_ssids = [wifi.group(1) for wifi in wifis if all(exclude not in wifi.group(1) for exclude in exclude)]
#     for ssid in valid_ssids:
#         if "LPU" in valid_ssids[0]:
#                 command = ['netsh', 'wlan', 'connect', 'name=' + ssid, 'ssid=' + ssid]
#                 result = subprocess.check_output(command)
#                 print(result)


    # print(result)

connect_to_wifi()
# logging_out()


