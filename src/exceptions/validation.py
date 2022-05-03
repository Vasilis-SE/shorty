from src.helpers.http_codes import HTTP_Codes


class Missing_Property(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, missing property..."
        self.http_code = HTTP_Codes.NOT_FOUND.value
        self.property = kwargs["property"] if 'property' in kwargs else ''
        super(Missing_Property, self).__init__(self.__dict__)


class Invalid_Type(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, invalid data type provided for property..."
        self.http_code = HTTP_Codes.BAD_REQUEST.value
        self.property = kwargs["property"] if 'property' in kwargs else ''
        super(Invalid_Type, self).__init__(self.__dict__)


class Invalid_Url(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, invalid url format provided..."
        self.http_code = HTTP_Codes.BAD_REQUEST.value
        super(Invalid_Url, self).__init__(self.__dict__)


class Invalid_Api_Provider(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, invalid provider given..."
        self.http_code = HTTP_Codes.BAD_REQUEST.value
        super(Invalid_Api_Provider, self).__init__(self.__dict__)
