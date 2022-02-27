from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pytest

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )
    parser.addoption(
        "--env", action="store", default="stg"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser = request.config.getoption('browser')
    environment = request.config.getoption('env')

    if browser == 'chrome':
        service = Service(r'D:/Dev/Selenium/drivers/chromedriver.exe')

        options = Options()
        options.add_argument('start-maximized')
        options.add_argument('--incognito')
        options.add_argument('--auto-open-devtools-for-tabs')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(
            service=service,
            options=options
        )
    elif browser == 'firefox':
        service = Service(r'D:/Dev/Selenium/drivers/geckodriver.exe')

        driver = webdriver.Firefox(service=service)
        driver.fullscreen_window()

    if environment == 'stg':
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif environment == 'uat':
        driver.get("https://www.google.com/")

    request.cls.driver = driver

    yield

    # driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the Pytest plugin to make and embed screenshot in html report, whenever test fails
    :param item:
    """
    pytest_html = item.config.pluginmanager.get_plugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace('::', '_') + '.png'
            _capture_screenshot(file_name)

            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"' \
                       'onClick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
