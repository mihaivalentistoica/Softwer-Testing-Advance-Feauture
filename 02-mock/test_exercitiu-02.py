from unittest.mock import Mock
from pytest import raises


def test_mock_key_error():
    mock = Mock()
    mock.get.side_effect = KeyError
    with raises(KeyError):
        mock.get()
    mock.get.assert_called()
    mock.get.side_effect = IndexError
    with raises(IndexError):
        mock.get()
    mock.get.assert_called()
