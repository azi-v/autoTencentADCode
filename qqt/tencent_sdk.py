import json
import random
import requests
import time

client_id = "*******"  # input("请输入client_id:")
client_secret = "***********"  # input("请输入client_secret:")
uri = "****************"  # input("请输入uri:")


class TencentSDK(object):
    def __init__(self):
        self.interface = 'oauth/token'
        self.url = 'https://api.e.qq.com/'
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = uri

    def oauth_token(self, authorization_code):

        url = self.url + self.interface

        common_parameters = {
            'timestamp': int(time.time()),
            'nonce': str(time.time()) + str(random.randint(0, 999999)),
        }

        parameters = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "authorization_code": authorization_code,
            "redirect_uri": self.redirect_uri
        }

        parameters.update(common_parameters)
        for k in parameters:
            if type(parameters[k]) is not str:
                parameters[k] = json.dumps(parameters[k])

        r = requests.get(url, params=parameters)

        return r.json()

    @staticmethod
    def user_action_sets_add(account_id, access_token):

        interface = 'user_action_sets/add'
        url = 'https://api.e.qq.com/v1.3/' + interface

        common_parameters = {
            'access_token': access_token,
            'timestamp': int(time.time()),
            'nonce': str(time.time()) + str(random.randint(0, 999999)),
        }

        parameters = {
            "account_id": account_id,
            "type": "WEB",
            "name": "webuser_action_set",
            "description": ""
        }
        r = requests.post(url, params=common_parameters, json=parameters)

        return r.json()
