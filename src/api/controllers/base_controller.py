from flask import jsonify, make_response


class Base_Controller():

    # Function that handles the response of the api
    def send(self, response):
        http_code = response['http_code']
        del response['http_code']
        final = make_response(jsonify(response), http_code)
        return final
