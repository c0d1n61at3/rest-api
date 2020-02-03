"""
Flask:
    1.  create_tables.py
"""
from database.sqlite import Sqlite


def create_users_table() -> None:
    with Sqlite() as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS main.users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')


def create_items_table() -> None:
    with Sqlite() as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS main.items (id INTEGER PRIMARY KEY, name TEXT, price REAL)')


if __name__ == '__main__':
    create_users_table()
    create_items_table()

    print('\n' * 2)

