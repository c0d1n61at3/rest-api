"""
Flask:
    1.  run.py
"""
from app import app
from database.sqlalchemy_db import sqla_db

sqla_db.init_app(app)


@app.before_first_request
def create_tables():
    sqla_db.create_all()


if __name__ == '__main__':
    print('\n' * 2)

