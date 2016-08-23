__author__ = 'Chad Peterson'
__email__ = 'chapeter@cisco.com'

import requests
import json

payload = {
    "id": "chapeter-1",
    "instances": 1,
    "cpus": 0.5,
    "mem": 32.0,
    "container": {
    "type": "DOCKER",
    "docker": {
    "image": "chapeter/devnet-hunt-1",
    "network": "BRIDGE",
    "portMappings": [
        { "containerPort": 80, "hostPort": 0 }
    ],
    "forcePullImage": True
    },
    "upgradeStrategy": {
    "minimumHealthCapacity": 0.5,
    "maximumOverCapacity": 3
    }
    }
}

url = "https://mantlsandbox.cisco.com/v2/apps"

headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46MXZ0R0Bsd0B5",
}

response = requests.post(url, data=payload, headers=headers, verify=False)

print response.text