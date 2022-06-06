import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .post_test_reports_to_slack import post_reports_to_slack


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

    "add parser options"
    parser.addoption("-I", "--slack_integration_flag",
                     dest="slack_integration_flag",
                     default="N",
                     help="Post the test report on slack channel: Y or N")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


# pytest plugin hook
def pytest_sessionfinish(session, exitstatus):
    "executes after whole test run finishes."
    if session.config.getoption('-I').lower() == 'y':
        post_reports_to_slack()