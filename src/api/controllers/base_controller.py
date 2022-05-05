from flask import jsonify, make_response


class Base_Controller():
    """ Base controller class that each controller inherits from and that
        it responds back to the requester so that there is a unified way to
        do this. It
    """

    # Function that handles the response of the api
    def send(self, response):
        http_code = response['http_code']
        del response['http_code']
        final = make_response(jsonify(response), http_code)
        return final
