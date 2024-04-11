import requests
import json

URL = "http://mini-challenge.foris.ai"

login_endpoint = "/login"
challenge_endpoint = "/challenge"
dumps_endpoint = "/dumps/mysql"
validate_endpoint = "/validate"


def login():
    body = {
        "username": "foris_challenge",
        "password": "ForisChallenge"
        }

    r = requests.post(url=(URL + login_endpoint), json=body)

    r_data = json.loads(r.text)
    return r_data["access_token"]

def challenge(token):

    challenge_r = requests.get(url=(URL + challenge_endpoint),
                            headers={"Authorization": "Bearer " + token})

    return challenge_r.text

def download_SQL_dump(token):

    database = requests.get(url=(URL + dumps_endpoint), headers={"Authorization": "Bearer " + token})

    return database

def validate_answer(token):
    body = {"number_of_groups": 168, "answer": 28}

    result = requests.post(url=(URL + validate_endpoint), headers={"Authorization": "Bearer " + token}, json=body)

    return result


if __name__ == "__main__":
    token = login()

    challenge_info = challenge(token)
    print(challenge_info)

    sql_dump = download_SQL_dump(token)
    with open("dump.sql", "wb") as f:
        f.write(sql_dump.content)
    
    data = validate_answer(token)
    print(data.text)
