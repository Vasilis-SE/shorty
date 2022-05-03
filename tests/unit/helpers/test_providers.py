import enum
from src.helpers.providers import Shortening_Providers


class Test_Shortening_Providers:
    def test_correct_data_type(self):
        assert type(Shortening_Providers) == enum.EnumMeta

    def test_is_enum_empty(self):
        assert len(Shortening_Providers._member_names_) > 0

    def test_has_enum_empty_values(self):
        for provider in Shortening_Providers:
            assert provider.value != None

    def test_http_codes_integrity(self):
        assert Shortening_Providers.BITLY.value == "shorten_url_bitly"
        assert Shortening_Providers.TINYURL.value == "shorten_url_tinyurl"
