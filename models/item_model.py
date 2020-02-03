"""
Flask:
    1.  item_model.py
"""
from typing import Dict

from database.sqlalchemy_db import sqla_db


class ItemModel(sqla_db.Model):
    __tablename__ = 'items'

    id = sqla_db.Column(sqla_db.Integer, primary_key=True)
    name = sqla_db.Column(sqla_db.String(25))
    price = sqla_db.Column(sqla_db.Float(precision=2))
    store_id = sqla_db.Column(sqla_db.Integer, sqla_db.ForeignKey('store.id'))
    # this is essentially the join between ItemModel and StoreModel
    store = sqla_db.relationship('StoreModel')

    def __init__(self, id_: int, name: str, price: float, store_id: int) -> None:
        self.id = id_
        self.name = name
        self.price = price
        self.store_id = store_id

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self._id}, name={self._name}, price={self._price})'

    def json(self) -> Dict:
        return {
            'name': self.name,
            'price': self.price
        }

    @classmethod
    def find_by_name(cls, name: str) -> __init__:
        return cls.query.filter_by(name=name).first()

    # NOTE: this is upsert
    def save_to_db(self) -> None:
        sqla_db.session.add(self)
        sqla_db.session.commit()

    def delete_from_db(self) -> None:
        sqla_db.session.delete(self)
        sqla_db.session.commit()


if __name__ == '__main__':
    print('\n' * 2)

