import pytest


@pytest.fixture()
def setup():
    print("this is setup")
    yield
    print("this is will last -yield")


@pytest.fixture()
def dataload():
    print("use data for login")
    return ["ketan","Hiray"]

@pytest.fixture(params=["chrome","firefox"])
def crossBrowser(request):
    return request.param