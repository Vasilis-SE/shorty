from src.api.models.shortener import Shortener_Model


class Test_Shortener_Model():

    def test_class_contains_methods(self):
        assert hasattr(Shortener_Model, 'shorten_url') and callable(
            getattr(Shortener_Model, 'shorten_url')) == True
        assert hasattr(Shortener_Model, 'get_url') and callable(
            getattr(Shortener_Model, 'get_url')) == True
        assert hasattr(Shortener_Model, 'get_provider') and callable(
            getattr(Shortener_Model, 'get_provider')) == True
        assert hasattr(Shortener_Model, 'set_url') and callable(
            getattr(Shortener_Model, 'set_url')) == True
        assert hasattr(Shortener_Model, 'set_provider') and callable(
            getattr(Shortener_Model, 'set_provider')) == True

    def test_init_instance_works(self):
        _model = Shortener_Model(
            url='https://google.com',
            provider='bitly'
        )

        assert _model.get_url() == 'https://google.com'
        assert _model.get_provider() == 'bitly'
