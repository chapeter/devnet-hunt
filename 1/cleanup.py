





import requests


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNoYXBldGVyIiwicm9sZSI6InVzZXIiLCJpYXQiOjE0NzE4OTcxNDMsImV4cCI6MTQ3MzEwNjc0M30.nPef98Cj_ibO2dzbQ3--pp0LR-EasoPDjlS5AesV6Gs"

url = "http://production--devnet-challe--devnet-challenge-api--53c63a.gce.shipped-cisco.com/challenges/chapeter"


headers = {
    'content-type': "application/json",
    'access_token': token,
    'cache-control': "no-cache",
}

response = requests.get(url, headers=headers).json()

for r in response:
    if r['id'] != '57bbaea641c7360100fd94ef':
        item = str(r['id'])
        url = "http://production--devnet-challe--devnet-challenge-api--53c63a.gce.shipped-cisco.com/challenges/answer/%s" % item

        payload = ""
        headers = {
            'content-type': "application/json",
            'access_token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNoYXBldGVyIiwicm9sZSI6InVzZXIiLCJpYXQiOjE0NzE4OTcxNDMsImV4cCI6MTQ3MzEwNjc0M30.nPef98Cj_ibO2dzbQ3--pp0LR-EasoPDjlS5AesV6Gs",
            'cache-control': "no-cache",
            'postman-token': "78ac880c-379b-3fb6-6643-8f78db9f8e90"
            }

        response = requests.request("DELETE", url, data=payload, headers=headers)

        print(response.text)