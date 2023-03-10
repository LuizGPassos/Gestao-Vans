from flask import request, current_app

class request_handler:
    def get_args():
        if request.method == 'POST':
            return request.form
        if request.method == 'GET':
            return request.args
        if request.method == 'DELETE':
            return request.form
        if request.method == 'PUT':
            return request.form