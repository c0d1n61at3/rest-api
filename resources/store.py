"""
Flask:
    1.  store.py
"""
from typing import Tuple

from flask_restful import Resource

from models.store_model import StoreModel


class Store(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self, name: str) -> Tuple:
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        else:
            return {'message': 'store not found'}, 404

    # noinspection PyMethodMayBeStatic
    def post(self, name: str) -> Tuple:
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': 'store already exists'}, 400
        else:
            store = StoreModel(None, name)
            # noinspection PyBroadException
            try:
                store.save_to_db()
            except Exception:
                return {'message': 'error occurred inserting store'}, 500
        return store.json(), 200

    # noinspection PyMethodMayBeStatic
    def delete(self, name: str) -> Tuple:
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'store deleted'}, 200


class Stores(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self) -> Tuple:
        # return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
        return {'stores': [store.json() for store in StoreModel.query.all()]}, 200


if __name__ == '__main__':
    print('\n' * 2)

