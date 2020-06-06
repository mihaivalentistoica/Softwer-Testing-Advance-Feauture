"""
1. Write a fixture returning a mocked database object:
    - count() with any parameters should return 1
    - list_tables() should return („users”)
    - get() should return a dictionary with username, first_name, last_name
      and email keys
2. Use the fixture and test each of those functions; Don't forget to check
   parameters passed to them.
"""

from unittest.mock import Mock
import pytest


@pytest.fixture()
def create_mock():
    database = Mock()
    database.count.return_value = 1
    database.list_values.return_value = ('users',)
    database.get.return_value = {"username": "username", "first_name": "First Name", "last_name": "Last Name",
                                 "email": "email@mail.com"}

    return database


def test_count(create_mock):
    create_mock.count.assert_not_called()
    assert create_mock.count() == 1
    create_mock.count.assert_called_once()


def test_list_values(create_mock):
    create_mock.list_values.assert_not_called()
    assert create_mock.list_values() == ("users",)
    create_mock.list_values.assert_called_once()


def test_get(create_mock):
    create_mock.get.assert_not_called()
    assert create_mock.get() == {"username": "username", "first_name": "First Name", "last_name": "Last Name",
                                 "email": "email@mail.com"}
    create_mock.get.assert_called_once()
