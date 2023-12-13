import subprocess
import requests
import socket
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning from urllib3 needed for this script. (read about this dumbo.. chatgpt)
urllib3.disable_warnings(InsecureRequestWarning)

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
                
            else:
                print(f"Good! Official LPU Stuff")
                
        else:
            print(f"Connect to any of the LPU Wireless Network (LPU Wireless, LPU Hostel)")
            
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

check_ssid_presence(target_ssid)
if check_ssid_presence(target_ssid)==true:
    loggin_in()

def logging_out():
    payload={'username':'12206717@lpu.com', 'password':'96148351', 'mode':'193', 'ipaddress':ip, 'logintype':'2', 'loggedinuser':'12206717@lpu.com', 'logout':'Logout'}
    r =requests.post('https://10.10.0.1/24online/servlet/E24onlineHTTPClient', verify=False, data=payload)
    r.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
    res = r.text
    if "To start surfing" in res:
        print("You have successfully logged off")
    else:
        print("Logout failed")




# logging_out()


