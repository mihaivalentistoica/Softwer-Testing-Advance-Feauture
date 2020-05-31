"""
When DB.get() is called:
    - With non-existent table_name it raises a KeyError
    - With non-existent index it raises an IndexError

Use Mock() with side_effect to make the tests in 02-mock/test_exercise-02.py run faster.
"""

import pytest
from db import DB


def test_get_with_non_existent_table():
    db = DB()
    with pytest.raises(KeyError):
        db.get("non-existent db", 1)


def test_get_with_non_index():
    db = DB()
    next_user_idx = db.count("users")
    with pytest.raises(IndexError):
        db.get("users", next_user_idx)
