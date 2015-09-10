__author__ = 'fritz'
import requests
from urllib.parse import urlencode
session = requests.session()
session.get("https://shop.rewe.de/")


def post(url, payload, check_for_success=True):
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8 "}
    payload.update({"token": session.cookies['secureToken']})
    payload = urlencode(payload)
    r = session.post(url,
                     headers=headers,
                     data=payload)

    if check_for_success:
        r = r.json()
        if not r.get('success'):
            raise Exception(r.get('errors'))
    return r


def get(url):
    r = session.get(url)
    return r


def login(username, password):
    url = "https://shop.rewe.de/login/submit/ajax"
    payload = {"username": username,
               "password": password}
    response = post(url, payload)
    if not response.get('success'):
        raise LoginException(response.get('errors'))


class LoginException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)