from src.api.models.bitly_shortener import Bitly_Shortener
from src.api.models.shortener import Shortener_Model

class Test_Bitly_Shortener():

    def test_contains_shorten_method(self):
        assert hasattr(Bitly_Shortener, 'shorten_url') and callable(
            getattr(Bitly_Shortener, 'shorten_url')) == True

    def test_inherits_from_shorten_model(self):
        assert issubclass(Bitly_Shortener, Shortener_Model) == True

    def test_shorten_method_should_fail(self):
        bitly = Bitly_Shortener(
            url="https://google.com",
            provider="bitly"
        )
        
        # Fails because there is no token set for the api
        assert bitly.shorten_url() == False