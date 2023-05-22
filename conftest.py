import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config_reader import config as cfg

class Driver(webdriver.Chrome):
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        webdriver.Chrome.__init__(self, service=Service(ChromeDriverManager().install()), options=options)

@pytest.fixture
def driver():
    driver = Driver()

    yield driver

    driver.quit()

@pytest.fixture
def config():
    return cfg()