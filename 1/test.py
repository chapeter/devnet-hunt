import requests

url = "https://mantlsandbox.cisco.com:8080/v2/apps"

payload = "{\n\"id\": \"chapeter-3\",\n\"instances\": 1,\n\"cpus\": 0.5,\n\"mem\": 32.0,\n\"container\": {\n\"type\": \"DOCKER\",\n\"docker\": {\n\"image\": \"chapeter/devnet-hunt-1\",\n\"network\": \"BRIDGE\",\n\"portMappings\": [\n{ \"containerPort\": 80, \"hostPort\": 0 }\n],\n\"forcePullImage\": true\n\n},\n\"upgradeStrategy\": {\n\"minimumHealthCapacity\": 0.5,\n\"maximumOverCapacity\": 3\n}\n}\n}"
headers = {
    'content-type': "application/json",
    'authorization': "Basic YWRtaW46MXZ0R0Bsd0B5",
    'cache-control': "no-cache",
    'postman-token': "cd6bb0df-03b6-7a53-4272-95be7f18c669"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)