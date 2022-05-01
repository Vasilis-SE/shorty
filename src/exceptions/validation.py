from src.helpers.http_codes import HTTP_Codes

class MissingProperty(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, missing property..."
        self.http_code = HTTP_Codes.NOT_FOUND.value
        self.property = kwargs["property"]
        super(MissingProperty, self).__init__(self.__dict__)

class InvalidType(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, invalid data type provided for property..."
        self.http_code = HTTP_Codes.BAD_REQUEST.value
        self.property = kwargs["property"]
        super(InvalidType, self).__init__(self.__dict__)

class InvalidUrl(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, invalid url format provided..."
        self.http_code = HTTP_Codes.BAD_REQUEST.value
        super(InvalidType, self).__init__(self.__dict__)