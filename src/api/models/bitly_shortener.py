from src.api.models.shortener import Shortener_Model


class Bitly_Shortener(Shortener_Model):
    
    def __init__(self, url, provider):
        super().__init__(url, provider)

    # Implement shortening of bitly provider
    def shorten_url(): 
        pass
