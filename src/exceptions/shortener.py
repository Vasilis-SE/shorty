from src.helpers.http_codes import HTTP_Codes


class Shortening_Failed(Exception):
    def __init__(self, **kwargs):
        self.message = kwargs["message"] if "message" in kwargs else "Error occurred, could not shorten the given URL..."
        self.http_code = HTTP_Codes.SERVER_ERROR.value
        super(Shortening_Failed, self).__init__(self.__dict__)
