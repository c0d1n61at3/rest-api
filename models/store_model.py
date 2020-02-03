"""
Flask:
    1.  store_model.py
"""
from typing import Dict

from database.sqlalchemy_db import sqla_db


class StoreModel(sqla_db.Model):
    __tablename__ = 'store'

    id = sqla_db.Column(sqla_db.Integer, primary_key=True)
    name = sqla_db.Column(sqla_db.String(25))

    # this is essentially the join between StoreModel and ItemModel
    # NOTE: lazy load items in store
    items = sqla_db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, id_: int, name: str) -> None:
        self.id = id_
        self.name = name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, name={self.name})'

    def json(self) -> Dict:
        return {
            'name': self.name,
            'items': [item.json() for item in self.items.all()]
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

