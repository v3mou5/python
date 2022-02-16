import socket
import platform
import re
import os
import requests
import subprocess

print(socket.gethostname())
print(platform.version())
print(platform.machine())
ip = requests.get('https://api.ipify.org').text.strip()
print(f'My public IP address is: {ip}')
base=subprocess.check_output("net user").decode('ascii').split('\n')
ctr=0
for line in base:
    if ctr==1:
        print(line)
        break
    if "Administrator" in line:
        ctr+=1
base2=subprocess.check_output("net localgroup").decode('ascii')
base3=subprocess.check_output("getmac").decode('ascii')
print(base2)
print(base3)
def get_wifi_pass():
    sub=subprocess.check_output('netsh wlan show profile').decode('utf-8').split('\n')
    newl=[]
    for line in sub:
        if "All User Profile" in line:
            newl.append(line.split(":")[1][1:-1])
    pa=[]
    for profile in newl:
        sub2=subprocess.check_output(['netsh','wlan','show','profile',profile,'key=clear']).decode('utf-8').split('\n')
        for line in sub2:
            if "Key Content" in line:
                pa.append(line.split(":")[1][1:-1])
    all_info=dict(zip(newl,pa))
    print(all_info)

        
get_wifi_pass()