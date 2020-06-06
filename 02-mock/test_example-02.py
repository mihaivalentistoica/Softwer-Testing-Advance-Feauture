from db import DB
from unittest.mock import Mock


def test_db_connection_real():
    db_real = DB()  # db simulates slow database connection
    assert len(db_real.list_tables()) == 3
    assert db_real.list_tables() == ("users", "products", "orders")


def test_db_connection_mock():
    db_mock = Mock()
    db_mock.list_tables.return_value = ("users", "products", "orders")
    assert len(db_mock.list_tables()) == 3
    assert db_mock.list_tables() == ("users", "products", "orders")
