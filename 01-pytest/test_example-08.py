import pytest


@pytest.fixture(scope="module")  # scope="function" is default
def populated_dict():
    return {i + 1: chr(i + 97) for i in range(26)}


def test_replacement(populated_dict):
    populated_dict[1] = "z"
    assert populated_dict[1] == "z"


def test_alphabet(populated_dict):
    # Fixture runs for every function
    assert populated_dict[1] == "a"
