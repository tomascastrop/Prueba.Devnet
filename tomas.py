import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://192.168.184.130/restconf/data/ietf-interfaces:interfaces/interface=Loopback55"
headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"
           }
basicauth = ("cisco", "cisco123!")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback55",
        "description": "tomas ccastro",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "172.16.55.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
