from src.exceptions.validation import Missing_Property, Invalid_Type, Invalid_Url, Invalid_Api_Provider


class Test_Missing_Property():

    def test_does_it_inherit_exception(self):
        assert issubclass(Missing_Property, Exception) == True

    def test_without_params_object_is_setup_correctly(self):
        missing_property_ex = Missing_Property()

        assert type(missing_property_ex.message) == str
        assert missing_property_ex.message != ''
        assert type(missing_property_ex.http_code) == int
        assert missing_property_ex.http_code == 404
        assert type(missing_property_ex.property) == str
        assert missing_property_ex.property == ''

    def test_with_params_object_is_setup_correctly(self):
        missing_property_ex = Missing_Property(
            message='this is an exception message',
            property='username'
        )

        assert type(missing_property_ex.message) == str
        assert missing_property_ex.message != ''
        assert missing_property_ex.message == 'this is an exception message'
        assert type(missing_property_ex.http_code) == int
        assert missing_property_ex.http_code == 404
        assert type(missing_property_ex.property) == str
        assert missing_property_ex.property == 'username'


class Test_Invalid_Type():

    def test_does_it_inherit_exception(self):
        assert issubclass(Invalid_Type, Exception) == True

    def test_without_params_object_is_setup_correctly(self):
        invalid_type_ex = Invalid_Type()

        assert type(invalid_type_ex.message) == str
        assert invalid_type_ex.message != ''
        assert type(invalid_type_ex.http_code) == int
        assert invalid_type_ex.http_code == 400
        assert type(invalid_type_ex.property) == str
        assert invalid_type_ex.property == ''

    def test_with_params_object_is_setup_correctly(self):
        invalid_type_ex = Invalid_Type(
            message='this is an exception message',
            property='username'
        )

        assert type(invalid_type_ex.message) == str
        assert invalid_type_ex.message != ''
        assert invalid_type_ex.message == 'this is an exception message'
        assert type(invalid_type_ex.http_code) == int
        assert invalid_type_ex.http_code == 400


class Test_Invalid_Url():

    def test_does_it_inherit_exception(self):
        assert issubclass(Invalid_Url, Exception) == True

    def test_without_params_object_is_setup_correctly(self):
        invalid_url_ex = Invalid_Url()

        assert type(invalid_url_ex.message) == str
        assert invalid_url_ex.message != ''
        assert type(invalid_url_ex.http_code) == int
        assert invalid_url_ex.http_code == 400

    def test_with_params_object_is_setup_correctly(self):
        invalid_url_ex = Invalid_Url(
            message='this is an exception message'
        )

        assert type(invalid_url_ex.message) == str
        assert invalid_url_ex.message != ''
        assert invalid_url_ex.message == 'this is an exception message'
        assert type(invalid_url_ex.http_code) == int
        assert invalid_url_ex.http_code == 400


class Test_Invalid_Api_Provider():

    def test_does_it_inherit_exception(self):
        assert issubclass(Invalid_Api_Provider, Exception) == True

    def test_without_params_object_is_setup_correctly(self):
        invalid_api_provider_ex = Invalid_Api_Provider()

        assert type(invalid_api_provider_ex.message) == str
        assert invalid_api_provider_ex.message != ''
        assert type(invalid_api_provider_ex.http_code) == int
        assert invalid_api_provider_ex.http_code == 400

    def test_with_params_object_is_setup_correctly(self):
        invalid_api_provider_ex = Invalid_Api_Provider(
            message='this is an exception message',
        )

        assert type(invalid_api_provider_ex.message) == str
        assert invalid_api_provider_ex.message != ''
        assert invalid_api_provider_ex.message == 'this is an exception message'
        assert type(invalid_api_provider_ex.http_code) == int
        assert invalid_api_provider_ex.http_code == 400
