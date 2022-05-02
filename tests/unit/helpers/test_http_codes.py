import enum
from src.helpers.http_codes import HTTP_Codes


class Test_HTTP_Codes:
    def test_correct_data_type(self):
        assert type(HTTP_Codes) == enum.EnumMeta

    def test_is_enum_empty(self):
        assert len(HTTP_Codes._member_names_) > 0

    def test_has_enum_empty_values(self):
        for http_code in HTTP_Codes:
            assert http_code.value != None

    def test_http_codes_integrity(self):
        assert HTTP_Codes.OK.value == 200
        assert HTTP_Codes.CREATED.value == 201
        assert HTTP_Codes.BAD_REQUEST.value == 400
        assert HTTP_Codes.UNAUTHORIZED.value == 401
        assert HTTP_Codes.FORBIDDEN.value == 403
        assert HTTP_Codes.NOT_FOUND.value == 404
        assert HTTP_Codes.SERVER_ERROR.value == 500
        assert HTTP_Codes.SERVICE_UNAVAILABLE.value == 503
