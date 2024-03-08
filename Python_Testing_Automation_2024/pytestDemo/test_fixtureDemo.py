import pytest


@pytest.mark.usefixtures("setup")
class TestDemo:

    def test_fixtureDemo1(self):
        print("this function will execute the fixture 1")

    def test_fixtureDemo2(self):
        print("this function will execute the fixture 1")

    def test_fixtureDemo3(self):
        print("this function will execute the fixture 3")
