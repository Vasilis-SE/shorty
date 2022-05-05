import json

import validators
from src.helpers.curl import Curl_Helper


class Test_E2E_Shortner():

    def test_invalid_provider_should_return_error(self):
        _curl = Curl_Helper()
        response = _curl.post(
            url="http://localhost:3000/api/v1/shortlinks",
            payload=json.dumps({
                "url": "https://google.com",
                "provider": "somethingWRONG"
            }),
            header={
                'Content-Type': 'application/json'
            }
        )

        assert response.status_code == 400
        response = response.text

        assert response != ''
        assert type(response) == str

        response = json.loads(response)
        assert response['message'] != ''

    def test_valid_provider_should_return_response(self):
        _curl = Curl_Helper()
        response = _curl.post(
            url="http://localhost:3000/api/v1/shortlinks",
            payload=json.dumps({
                "url": "https://google.com",
                "provider": "tinyurl"
            }),
            header={
                'Content-Type': 'application/json'
            }
        )

        assert response.status_code == 200
        response = response.text

        assert response != ''
        assert type(response) == str

        response = json.loads(response)
        assert response['link'] != ''
        assert response['url'] != ''
        assert validators.url(response['link']) == True
        assert validators.url(response['url']) == True

    def test_unimplemented_provider_fallback(self):
        _curl = Curl_Helper()
        response = _curl.post(
            url="http://localhost:3000/api/v1/shortlinks",
            payload=json.dumps({
                "url": "https://google.com",
                "provider": "bitly"
            }),
            header={
                'Content-Type': 'application/json'
            }
        )

        assert response.status_code == 200
        response = response.text

        assert response != ''
        assert type(response) == str

        response = json.loads(response)
        assert response['link'] != ''
        assert response['url'] != ''
        assert validators.url(response['link']) == True
        assert validators.url(response['url']) == True
