import pytest


@pytest.mark.smoke
def test_firstProgram():
    msg = "hello"
    assert msg == "hi"


def test_firstSecondProgram():
    a = 3
    b = 3
    assert a == b

