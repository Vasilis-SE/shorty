class Shortener_Model():
    """ This is the basic model that sets all the core features 
        for a shortening provider implementation. Any new API 
        implementation class must inherit from this one and use the
        shorten_url mehtod to implement its logic.

        Properties:
            url         The url that will be shortened by the X provider.
            provider    The provider's name that will shorten the url.    

    """

    def __init__(self, url, provider):
        self.set_url(url)
        self.set_provider(provider)

    def shorten_url():
        pass

    def get_url(self):
        return self.url

    def get_provider(self):
        return self.provider

    def set_url(self, url):
        self.url = url

    def set_provider(self, provider):
        self.provider = provider
