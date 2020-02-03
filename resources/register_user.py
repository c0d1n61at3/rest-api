"""
Flask:
    1.  user_register.py
"""
from typing import Tuple

from flask_restful import Resource, reqparse

from models.user_model import UserModel


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='username is required')
    parser.add_argument('password', type=str, required=True, help='password is required')

    # noinspection PyMethodMayBeStatic
    def post(self) -> Tuple:
        json_payload = RegisterUser.parser.parse_args()
        if UserModel.find_by_username(json_payload.get('username', None)):
            return {'message': 'username already exists'}, 400

        user = UserModel(None, **json_payload)
        user.save_to_db()
        return {'message': 'user created'}, 201


if __name__ == '__main__':
    print('\n' * 2)

