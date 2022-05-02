import os
from src.api.models.shortener import Shortener_Model
from bitly_api import Connection, BitlyError

class Bitly_Shortener(Shortener_Model):
    
    def __init__(self, url, provider):
        super().__init__(url, provider)

    # Implement shortening of bitly provider
    def shorten_url(self): 
        try:
            bitly = Connection(access_token=os.getenv('BITLY_ACCESS_TOKEN'))
            shortened_url = bitly.shorten(self.url)
            return shortened_url
        except BitlyError as ex:
            return self.url