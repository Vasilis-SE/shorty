import os
from src.api.models.shortener import Shortener_Model

class Tinyurl_Shortener(Shortener_Model):
    
    def __init__(self, url, provider):
        super().__init__(url, provider)

    # Implement shortening of bitly provider
    def shorten_url(self): 
        try:
            pass
        except Exception as ex:
            return self.url