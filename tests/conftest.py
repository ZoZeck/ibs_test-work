import yaml
import pytest
import requests

from chromedriver_py import binary_path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class Driver(webdriver.Chrome):
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
        webdriver.Chrome.__init__(self, service=Service(binary_path), options=options)

    @property
    def main_page_upgrade_button(self):
        return self.find_element(By.XPATH, "//*[text() = 'Upgrade']")
    
    @property
    def main_page_proform_section(self):
        return self.find_element(By.XPATH, "//div[@id = 'pro-form']")
    
    @property
    def main_page_subscribe_button(self):
        return self.find_element(By.XPATH, "//input[@value= 'Subscribe']")
    
    @property
    def main_page_email_input(self):
        return self.find_element(By.XPATH, "//input[@type= 'email']")
    
    @property
    def subscribe_page_return_button(self):
        return self.find_element(By.XPATH, "//a[text() = '« return to our website']")
    
    @property
    def subscribe_page_submit_button(self):
        return self.find_element(By.XPATH, "//input[@type = 'submit']")
    
    @property
    def main_page_swagger(self):
        return self.find_element(By.XPATH, "//*[@class = 'swagger-link']")
    
    @property
    def scroll_position(self):
        return self.execute_script("return window.pageYOffset;")
    
    @property
    def main_page_sailsjs_button(self):
        return self.find_element(By.XPATH, "//*[text() = 'Sailsjs']")

    @property
    def main_page_amount_input(self):
        return self.find_element(By.XPATH, "//input[@type= 'number']")
    
    @property
    def main_page_support_reqres_button(self):
        return self.find_element(By.XPATH, "//button[text()= 'Support ReqRes']")
    
    @property
    def main_page_support_one_time_check_box(self):
        return self.find_element(By.XPATH, "//input[@value= 'supportOneTime']")

    @property
    def main_page_support_recurring_check_box(self):
        return self.find_element(By.XPATH, "//input[@value= 'supportRecurring']")
    
    @property
    def payment_page_total_amount(self):
        return self.find_element(By.XPATH, "//*[@id = 'ProductSummary-totalAmount']//span")
        
    

@pytest.fixture
def driver(config):
    driver = Driver()

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture
def config():
    with open('config.yml') as yml:
        config = yaml.safe_load(yml)
        return config
