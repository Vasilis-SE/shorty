from src.helpers.curl import Curl_Helper
from src.api.models.shortener import Shortener_Model


class Tinyurl_Shortener(Shortener_Model):

    def __init__(self, url, provider):
        super().__init__(url, provider)

    # Implement shortening of tinyurl provider
    def shorten_url(self):
        try:
            curl = Curl_Helper()
            shortened_url = curl.get(
                url="https://tinyurl.com/api-create.php?url=" + self.url)
            return shortened_url
        except Exception as ex:
            return self.url
