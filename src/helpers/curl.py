import requests


class Curl_Helper():

    def __init__(self):
        pass

    def get(self, url, **header):
        response = requests.request("GET", url, headers=header)
        return response.text
