from src.helpers.curl import Curl_Helper
from src.api.models.shortener import Shortener_Model


class Tinyurl_Shortener(Shortener_Model):
    """ Model class that implements the tinyurl shortener API. 
        This class is part of the data layer of the application
        and as a model is the one tha communicates with the third party
        api. Also it inherits from Shortener_Model which sets the 
        core features of a shortener implementation.  
    """

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
            return False
