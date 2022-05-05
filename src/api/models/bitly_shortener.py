import os
from src.api.models.shortener import Shortener_Model
from bitly_api import Connection, BitlyError


class Bitly_Shortener(Shortener_Model):
    """ Model class that implements the bitly shortener API. 
        This class is part of the data layer of the application
        and as a model is the one tha communicates with the third party
        api. Also it inherits from Shortener_Model which sets the 
        core features of a shortener implementation.  
    """

    def __init__(self, url, provider):
        super().__init__(url, provider)

    # Implement shortening of bitly provider
    def shorten_url(self):
        try:
            bitly = Connection(access_token=os.getenv('BITLY_ACCESS_TOKEN'))
            shortened_url = bitly.shorten(self.url)
            return shortened_url
        except BitlyError as ex:
            return False
