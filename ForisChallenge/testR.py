import requests
import json

URL = "http://mini-challenge.foris.ai"

login_endpoint = "/login"
challenge_endpoint = "/challenge"

body = {"username": "foris_challenge", "password": "ForisChallenge"}

def login():
    response = requests.post(url=(URL + login_endpoint), json=body)
    
    data = json.loads(response.text)

    print(type(data))

    return data["access_token"]

def challenge(token):
    response = requests.get(url=(URL + challenge_endpoint),
                            headers={"Authorization" : "Bearer " + token })
    print(response.text)

if __name__ == "__main__":
    token = login()
    print(type(token))
    challenge(token)