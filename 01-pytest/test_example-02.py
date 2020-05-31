from pytest import raises


def test_greeen():
    assert 1 > 0


def test_identity_fail():
    assert False is False


def test_exception_fail():
    with raises(ZeroDivisionError):
        assert 1 / 0
