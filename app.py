"""
Flask:
    1.  app.py
"""
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, Items
from resources.register_user import RegisterUser
from resources.store import Store, Stores
from secure import authenticate, identity

app = Flask(__name__)
# NOTE: https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'
api = Api(app)
# NOTE: JWT() will create the /auth endpoint
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')
api.add_resource(RegisterUser, '/register')


if __name__ == '__main__':
    from database.sqlalchemy_db import sqla_db
    sqla_db.init_app(app)

    # NOTE: default port is 5000
    app.run(port=5000, debug=True)

    print('\n' * 2)

