from selenium.webdriver.common.by import By

class PaymentPageLocators:
    TOTAL_AMOUNT = (By.XPATH, "//*[@id = 'ProductSummary-totalAmount']//span")