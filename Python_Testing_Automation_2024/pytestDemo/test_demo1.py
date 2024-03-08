import pytest


def test_firstProgram(setup):
    print("hello pytest")
@pytest.mark.smoke
def test_secondProgram():
    print("how are you?")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

