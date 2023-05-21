from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def window_hendler(driver, main_window):
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)


def test_heroku_button(config, driver):
    driver.get(config['url']['body'])

    heroku_button = driver.find_element(By.XPATH, "//*[text() = 'Heroku']")
    heroku_button_href = heroku_button.get_attribute("href")
    assert heroku_button_href == config['url']['selenium']['heroku']
    heroku_button.click()
    assert driver.current_url == config['url']['selenium']['heroku']
    

def test_top_support_button(config, driver):
    driver.get(config['url']['body'])
    
    wait = WebDriverWait(driver, 0.5)

    initial_scroll_position = driver.scroll_position

    top_support_button = driver.find_element(By.XPATH, "//a[text()= 'Support ReqRes']")
    top_support_button.click()

    final_scroll_position = driver.scroll_position
    
    assert initial_scroll_position != final_scroll_position

def test_main_support_button_first_method(config, driver):
    driver.get(config['url']['body'])
    
    wait = WebDriverWait(driver, 5)
    amount = 9

    driver.main_page_support_one_time_check_box.click()

    amount_input = driver.main_page_amount_input
    amount_input.send_keys(amount)

    driver.main_page_support_reqres_button.click()
    
    assert wait.until(EC.url_contains(config['url']['selenium']['payment']))
    
    driver.implicitly_wait(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id = 'ProductSummary-totalAmount']//span")))
    actual_amount = int(driver.payment_page_total_amount.text.replace('$','')[:-3])
    
    assert actual_amount == amount


def test_main_support_button_second_method(config, driver):
    driver.get(config['url']['body'])

    wait = WebDriverWait(driver, 5)

    driver.main_page_support_recurring_check_box.click()
    driver.main_page_support_reqres_button.click()

    driver.implicitly_wait(5)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id = 'ProductSummary-totalAmount']//span")))
    actual_amount = int(driver.payment_page_total_amount.text.replace('$','')[:-3])

    assert actual_amount == 5


def test_upgrade_button(config, driver):
    driver.get(config['url']['body'])

    upgrade_button = driver.main_page_upgrade_button
    proform_section = driver.main_page_proform_section

    assert len(upgrade_button.get_attribute('style')) == 0 and len(proform_section.get_attribute('style')) == 0

    upgrade_button.click()

    assert upgrade_button.get_attribute('style') == 'display: none;' and proform_section.get_attribute('style') == 'display: block;'

def test_subscribe_button_without_email(config, driver):
    driver.get(config['url']['body'])

    main_window = driver.current_window_handle

    driver.main_page_upgrade_button.click()
    
    subsctibe_button = driver.main_page_subscribe_button
    subsctibe_button.click()

    window_hendler(driver, main_window)

    assert driver.current_url.startswith(config['url']['selenium']['benhowdle'])
    assert driver.subscribe_page_submit_button


def test_subscribe_button_with_email(config, driver):
    driver.get(config['url']['body'])

    main_window = driver.current_window_handle

    driver.main_page_upgrade_button.click()
    driver.main_page_email_input.send_keys('123@gmail.com')
    driver.main_page_subscribe_button.click()

    window_hendler(driver, main_window)

    assert driver.current_url.startswith(config['url']['selenium']['benhowdle'])
    assert driver.subscribe_page_return_button

def test_swagger_button(config, driver):
    driver.get(config['url']['body'])

    swagger = driver.main_page_swagger
    swagger.click()

    assert driver.current_url.startswith(config['url']['selenium']['swagger_dock'])

def test_sailsjs_button(config, driver):
    driver.get(config['url']['body'])

    sailsjs_button = driver.main_page_sailsjs_button
    sailsjs_button.click()
    assert driver.current_url.startswith(config['url']['selenium']['sailsjs'])