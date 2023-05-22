from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_SUPPORT_BUTTON = (By.XPATH, "//a[text()= 'Support ReqRes']")
    UPGRADE_BUTTON = (By.XPATH, "//*[text() = 'Upgrade']")
    PROFORM_SECTION = (By.XPATH, "//div[@id = 'pro-form']")
    SUBSCRIBE_BUTTON = (By.XPATH, "//input[@value= 'Subscribe']")
    EMAIL_INPUT = (By.XPATH, "//input[@type= 'email']")
    SWAGGER = (By.XPATH, "//*[@class = 'swagger-link']")
    SAILSJS_BUTTON = (By.XPATH, "//*[text() = 'Sailsjs']")
    AMOUNT_INPUT = (By.XPATH, "//input[@type= 'number']")
    SUPPORT_REQRES_BUTTON = (By.XPATH, "//button[text()= 'Support ReqRes']")
    SUPPORT_ONE_TIME_CHECK_BOX = (By.XPATH, "//input[@value= 'supportOneTime']")
    SUPPORT_RECURRING_CHECK_BOX = (By.XPATH, "//input[@value= 'supportRecurring']")
    HEROKU_BOTTON = (By.XPATH, "//*[text() = 'Heroku']")
    DESIGNED_BY = (By.XPATH, "//*[text() = 'Ben Howdle']")