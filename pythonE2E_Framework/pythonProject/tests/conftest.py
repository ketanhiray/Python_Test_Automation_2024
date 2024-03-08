import pytest
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C://chromedriver.exe")
        d = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj = Service("C://geckodriver.exe")
        d = webdriver.Firefox(service=service_obj)

    d.get("https://rahulshettyacademy.com/angularpractice/")
    d.implicitly_wait(5)
    d.maximize_window()
    request.cls.d = d
    yield
    d.close()
