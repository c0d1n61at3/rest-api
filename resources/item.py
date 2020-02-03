"""
Flask:
    1.  item.py
"""
from typing import Tuple

from flask_jwt import jwt_required
from flask_restful import Resource, reqparse, request

from models.item_model import ItemModel


# NOTE: using Api, there is no longer a need to use jsonify()
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='price is required')
    parser.add_argument('store_id', type=int, required=True, help='store_id is required')

    # noinspection PyMethodMayBeStatic
    @jwt_required()
    def get(self, name: str) -> Tuple:
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {
            'message': 'item not found'
        }, 404

    # noinspection PyMethodMayBeStatic
    def post(self, name: str) -> Tuple:
        found = ItemModel.find_by_name(name)
        if found:
            return {'message': 'item already exists'}, 400
        if request.is_json:
            json_payload = Item.parser.parse_args()
            new_item = ItemModel(None, name, **json_payload)
            # noinspection PyBroadException
            try:
                new_item.save_to_db()
            except Exception:
                return {'message': 'error occurred inserting item'}, 500
            return new_item.json(), 200
        return {
            'message': 'invalid json request'
        }, 400

    # noinspection PyMethodMayBeStatic
    def delete(self, name: str) -> Tuple:
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item deleted'}, 200

    # noinspection PyMethodMayBeStatic
    def put(self, name: str) -> Tuple:
        if request.is_json:
            json_payload = Item.parser.parse_args()
            item = ItemModel.find_by_name(name)
            if item:
                item.price = json_payload.get('price', None)
            else:
                item = ItemModel(None, name, **json_payload)

            # noinspection PyBroadException
            try:
                item.save_to_db()
            except Exception:
                return {'message': 'error occurred inserting item'}, 500
            return item.json(), 200
        return {
            'message': 'invalid json request'
        }, 400


class Items(Resource):
    # noinspection PyMethodMayBeStatic
    def get(self) -> Tuple:
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        return {'items': [item.json() for item in ItemModel.query.all()]}, 200


if __name__ == '__main__':
    print('\n' * 2)

