import pytest
from selenium import webdriver
@pytest.fixture()
def setup(request_browser):
    if request_browser=='chrome':
        driver=webdriver.Chrome()
        return driver
    else:
        driver=webdriver.Chrome()
        return driver

def pytest_addoption(parser): # method name must be pytest_addoption
    parser.addoption('--browser')
@pytest.fixture()
def request_browser(request):
    return request.config.getoption('--browser')

#code for capturing log reports to html report
# conftest.py
#
# def setup(request_browser):
#     driver=webdriver.Chrome()
#     return driver