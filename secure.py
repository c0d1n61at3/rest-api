"""
Flask:
    1.  secure.py
"""
from typing import Dict

from werkzeug.security import safe_str_cmp

from models.user_model import UserModel


# user needs to authenticate before using an JET secured endpoint, JWT token is returned after authentication
def authenticate(username: str, password: str) -> UserModel:
    user: UserModel = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


# endpoints secured by JWT, need the JWT <token> in HTTP header
def identity(payload: Dict) -> UserModel:
    id_ = payload.get('identity', None)
    return UserModel.find_by_id(id_)


if __name__ == '__main__':
    print('\n' * 2)

