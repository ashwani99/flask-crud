from flask import jsonify, make_response

class ApiException(Exception):
    def __init__(self, errors=["Something went wrong"], status_code=500):
        self.errors = errors
        self.status_code = status_code

    def to_json(self):
        return make_response(jsonify(errors=self.errors), self.status_code)
        