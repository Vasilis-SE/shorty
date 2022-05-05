from src.api.models.tinyurl_shortener import Tinyurl_Shortener
from src.api.models.shortener import Shortener_Model


class Test_Bitly_Shortener():

    def test_contains_shorten_method(self):
        assert hasattr(Tinyurl_Shortener, 'shorten_url') and callable(
            getattr(Tinyurl_Shortener, 'shorten_url')) == True

    def test_inherits_from_shorten_model(self):
        assert issubclass(Tinyurl_Shortener, Shortener_Model) == True

    def test_shorten_method_should_work(self):
        tinyurl = Tinyurl_Shortener(
            url="https://google.com",
            provider="tinyurl"
        )

        shortened_url = tinyurl.shorten_url()
        assert shortened_url != ''
        assert type(shortened_url) == str
