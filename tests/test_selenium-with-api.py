import json
import pytest

from conftest import Driver
from requests import request

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def test_similarity():
    data = []

    driver = Driver()
    
    driver.get('https://reqres.in')

    for element in driver.find_elements(By.XPATH, "//div[@class = 'endpoints']//ul//li"):
        element.click()

        wait = WebDriverWait(driver, 0.1)

        method = element.get_attribute("data-http").upper()
        url = element.find_element(By.XPATH, ".//a").get_attribute("href")
 
        try:
            wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//*[@data-key = 'output-request']")))
        except TimeoutException:
            pass

        params_text = driver.find_element(By.XPATH, "//*[@data-key = 'output-request']").text
        params = json.loads(params_text) if len(params_text) > 0 else {}

        req = request(method, url, json=params)

        response_text = driver.find_element(By.XPATH, "//*[@data-key = 'output-response']").text
        response = response_text if len(response_text) > 0 else '{' + '}'

        code = int(driver.find_element(By.XPATH, "//*[@data-key = 'response-code']").text)

        yield req.status_code, code, req.text if len(req.text) > 0 else '{' + '}', response


@pytest.mark.parametrize('code_req, code_sel, response_req, response_sel', test_similarity())
def test_compare_database(code_req, code_sel, response_req, response_sel):
    # Если нужна будет проверка с отсутвующим временем создания
    # if 'updatedAt' in  response_req and response_sel:
    #     res_req, res_sel = json.loads(response_req), json.loads(response_sel)
    #     res_req.pop('updatedAt'), res_sel.pop('updatedAt')
    #     assert code_req == code_sel and res_req == res_sel
    # else:
        assert code_req == code_sel and json.loads(response_req) == json.loads(response_sel)