from src.helpers.curl import Curl_Helper

class Test_Curl_Helper:

    def test_get_method(self):
        _curl = Curl_Helper()
        response = _curl.get('https://api2.binance.com/api/v3/ticker/price')

        assert response != None
        assert response != ''
        assert type(response) == str