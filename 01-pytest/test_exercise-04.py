from collections import Counter
import pytest


def is_anagram(word, other_word):
    """is_anagram checks whether other_word is an anagram of word"""
    if len(word) == 0 or len(other_word) == 0:
        return False
    return Counter(word) == Counter(other_word)


# print(is_anagram('baste', 'beast'))

def validate_coordinates(latitude, longitude):
    """validate_coordinates checks whether provided latitude and 
    longitude constitute a valid pair of GPS coordinates"""
    return -90.0 <= latitude <= 90 and -180.0 <= longitude <= 180.0


@pytest.mark.parametrize('word, other_word, expected_result',
                         [
                             ("beast", "beats", True),
                             ("dealing", "Leading", False),
                             ("Ana", "dealing", False),
                             ("rates", 'stare', True),
                             ("asd", "sda", True),
                             ("", "", False),
                             ("sda", "", False)
                         ])
def test_is_anagram(word, other_word, expected_result):
    assert is_anagram(word, other_word) is expected_result
