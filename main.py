import requests
import time
import json
import string
import secrets

base_url = "https://api.mail.tm/"
headers = {
    "Content-Type": "application/json"
}

def create_random_name():
    symbols = string.ascii_letters + string.digits
    mail_name = ''
    for i in range(12):
        mail_name += ''.join(secrets.choice(symbols))
    return mail_name + "@triots.com"


def create_mail(name):
    payload = {
        "address": name,
        "password": "lolsuprisedoll"
    }

    r = requests.post(base_url + "accounts", headers=headers, data=json.dumps(payload))
    time.sleep(2)
    print(r.status_code)
    response = r.json()
    print(response)

def main():
    print("WOrk")
    name = create_random_name()
    create_mail(name)


if __name__ == "__main__":
    main()