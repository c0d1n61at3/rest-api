"""
Flask:
    1.  user_model.py
"""

from database.sqlalchemy_db import sqla_db


class UserModel(sqla_db.Model):
    __tablename__ = 'users'

    id = sqla_db.Column(sqla_db.Integer, primary_key=True)
    username = sqla_db.Column(sqla_db.String(25))
    password = sqla_db.Column(sqla_db.String(25))

    def __init__(self, id_: int, username: str, password: str) -> None:
        self.id = id_
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username: str) -> __init__:
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id_: int) -> __init__:
        return cls.query.filter_by(id=id_).first()

    # NOTE: this is upsert
    def save_to_db(self) -> None:
        sqla_db.session.add(self)
        sqla_db.session.commit()

    def delete_from_db(self) -> None:
        sqla_db.session.delete(self)
        sqla_db.session.commit()


if __name__ == '__main__':
    print('\n' * 2)

