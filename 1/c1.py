import requests
import json
from flask import Flask

app = Flask(__name__)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNoYXBldGVyIiwicm9sZSI6InVzZXIiLCJpYXQiOjE0NzE4OTcxNDMsImV4cCI6MTQ3MzEwNjc0M30.nPef98Cj_ibO2dzbQ3--pp0LR-EasoPDjlS5AesV6Gs"



def submitAnswer(answer, token):

    url = "http://production--devnet-challe--devnet-challenge-api--53c63a.gce.shipped-cisco.com/challenges/"

    payload = {"name": "challenge1", "answer": answer}

    headers = {
        'content-type': "application/json",
        'access_token': token,
        'cache-control': "no-cache",
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers).json()

    return response

@app.route("/")
def getAnswer():
    url = "https://1faoejtuza.execute-api.us-east-1.amazonaws.com/prod/gsx-challenge"

    headers = {
        'content-type': "application/json"
    }

    response = requests.get(url, headers=headers)

    return response.text





if __name__ == "__main__":
    app.run(host='0.0.0.0')