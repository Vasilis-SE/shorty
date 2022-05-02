import json
import requests


class Curl_Helper():

    def __init__(self):
        pass

    def get(self, url, **header):
        response = requests.request("GET", url, headers=header)
        return response.text

    def post(self, url, payload, **header):
        payload = json.dumps(payload)
        response = requests.request("POST", url, headers=header, data=payload)
        return response.text

    def put(self, url, payload, **header):
        payload = json.dumps(payload)
        response = requests.request("PUT", url, headers=header, data=payload)
        return response.text

    def patch(self, url, payload, **header):
        payload = json.dumps(payload)
        response = requests.request("PATCH", url, headers=header, data=payload)
        return response.text

    def delete(self, url):
        response = requests.get("DELETE", url)
        return response.text
