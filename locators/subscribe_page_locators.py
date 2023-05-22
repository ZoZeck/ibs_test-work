from selenium.webdriver.common.by import By

class SubscribePageLocators:
    RETURN_BUTTON = (By.XPATH, "//a[text() = '« return to our website']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type = 'submit']")
    ERROR_MESSAGE = (By.XPATH, "//*[text() = 'There are errors below']")