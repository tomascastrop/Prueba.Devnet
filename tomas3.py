import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = { "ip": "192.168.184.130",
"device_type": "cisco_ios",
"username": "cisco",
"password": "cisco123!",
}
command = "show run"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)
    print()
    print(output)
    print()

