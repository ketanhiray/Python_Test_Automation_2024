import pytest
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium import webdriver

d = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global d
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


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    d.get_screenshot_as_file(name)
