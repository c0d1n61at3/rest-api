"""
Flask:
    1.  sqlite.py
"""
import sqlite3


# database context manager
class Sqlite:
    def __init__(self, database: str = 'data.db') -> None:
        self._database = database
        self._connection = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(database={self._database})'

    def __enter__(self) -> sqlite3.Connection:
        self._connection = sqlite3.connect(self._database)
        return self._connection

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> bool:
        if exc_type:
            self._connection.rollback()
            self._connection.close()
        else:
            self._connection.commit()
            self._connection.close()
        return False


if __name__ == '__main__':
    print('\n' * 2)

