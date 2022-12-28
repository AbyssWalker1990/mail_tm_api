import requests
import time
import json
import string
import secrets

base_url = "https://api.mail.tm/"
headers = {
    "Content-Type": "application/json"
}

# створює рандомну назву для пошти
def create_random_name():
    symbols = string.ascii_letters + string.digits
    mail_name = ''
    for i in range(12):
        mail_name += ''.join(secrets.choice(symbols))
    return mail_name.lower() + "@triots.com"

# Створює пошту з рандомною назвою
def create_mail(name):
    payload = {
        "address": name,
        "password": "lolsuprisedoll"
    }
    r = requests.post(base_url + "accounts", headers=headers, data=json.dumps(payload))
    time.sleep(2)
    print(r.status_code)
    response = r.json()
    print("MAIL CREATED: ", response)
    return payload


# Беремо токен, формуємо новий хедерс вже з авторизацією
def grab_token(credentials):
    payload = credentials
    print("CREDENTIALS: ", payload)
    r = requests.post(base_url + "token", headers=headers, data=json.dumps(payload))
    time.sleep(2)
    print(r.status_code)
    response = r.json()
    token = response.get('token')
    headers_with_token = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}",
    }
    print("New HEADER: ", headers_with_token)
    return headers_with_token



# Дістає тему і тіло листа, працюватиме корректно тільки якщо лист надходить 1
# Повинно викликатись після того як лист прийде!!!
def take_messages(headers_token):
    r = requests.get(base_url + "messages", headers=headers_token)
    print(r.status_code)
    messages = r.json().get('hydra:member')
    subject = messages[0].get('subject')
    intro = messages[0].get('intro')
    print("Subject: ", subject)
    print("Intro: ", intro)


# Основна функція
def main():
    print("WOrk")
    name = create_random_name()
    mail_data = create_mail(name)
    headers_with_token = grab_token(mail_data)
    # ТУТ ПОВИНЕН БУТИ СКРИПТ ЯКИЙ ПРИЗВОДИТЬ ДО НАДХОДЖЕННЯ ЛИСТА НА ПОШТУ, АБО СЛІП НА ПРОМІЖОК ЧАСУ, ЩО ПОТРІБНИЙ НА НАДХОДЖЕННЯ ЛИСТА
    # take_messages(headers_with_token)



if __name__ == "__main__":
    main()