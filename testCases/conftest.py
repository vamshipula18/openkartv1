import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


#******HTML Reports Generating Hooks******#

def pytest_configure(config):
    config._metadata['Project Name'] = 'OpenCart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Vamshi'


def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    path_dir = r"C:\Users\vamsh\PycharmProjects\openKartV1\reports"
    config.option.htmlpath = os.path.join(path_dir, "HtmlReports") + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
