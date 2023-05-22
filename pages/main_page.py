import allure
from allure_commons.types import AttachmentType

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as MainLocators
from locators.payment_page_locators import PaymentPageLocators as PaymentLocators
from locators.subscribe_page_locators import SubscribePageLocators as SubscribeLocators

class MainPage(BasePage):

    def heroku_button(self, config):
        heroku_button = self.element_is_visible(MainLocators.HEROKU_BOTTON)
        heroku_button_href = heroku_button.get_attribute("href")
        assert heroku_button_href == config['additional_url']['heroku']
        heroku_button.click()
        assert self.driver.current_url == config['additional_url']['heroku']


    def top_support_button(self):
        initial_scroll_position = self.scroll_position()

        top_support_button = self.element_is_visible(MainLocators.TOP_SUPPORT_BUTTON)
        top_support_button.click()

        final_scroll_position = self.scroll_position()
        
        assert initial_scroll_position != final_scroll_position


    def main_support_button_first_method(self, config):
        amount = 9

        self.element_is_visible(MainLocators.SUPPORT_ONE_TIME_CHECK_BOX).click()
        self.element_is_visible(MainLocators.AMOUNT_INPUT).send_keys(amount)
        self.element_is_visible(MainLocators.SUPPORT_REQRES_BUTTON).click()
        
        assert self.url_check(config['additional_url']['payment_page'])
        total_amount = self.element_is_visible(PaymentLocators.TOTAL_AMOUNT)
        actual_amount = int(total_amount.text.replace('$','')[:-3])
    
        assert actual_amount == amount


    def main_support_button_second_method(self, config):
        amount_by_default = 5

        self.element_is_visible(MainLocators.SUPPORT_RECURRING_CHECK_BOX).click()
        self.element_is_visible(MainLocators.SUPPORT_REQRES_BUTTON).click()

        assert self.url_check(config['additional_url']['payment_page'])
        total_amount = self.element_is_visible(PaymentLocators.TOTAL_AMOUNT)
        actual_amount = int(total_amount.text.replace('$','')[:-3])

        assert actual_amount == amount_by_default


    def upgrade_button(self):
        upgrade_button = self.element_is_visible(MainLocators.UPGRADE_BUTTON)
        proform_section = self.driver.find_element(*MainLocators.PROFORM_SECTION) # Использую * для того что бы преобразовать локатор в string

        assert len(upgrade_button.get_attribute('style')) == 0 and len(proform_section.get_attribute('style')) == 0

        upgrade_button.click()

        assert upgrade_button.get_attribute('style') == 'display: none;' and proform_section.get_attribute('style') == 'display: block;'


    def subscribe_button_without_email(self, config):
        main_window = self.driver.current_window_handle

        self.element_is_visible(MainLocators.UPGRADE_BUTTON).click()
        
        self.element_is_visible(MainLocators.SUBSCRIBE_BUTTON).click()

        self.window_hendler(main_window)

        assert self.driver.current_url.startswith(config['additional_url']['benhowdle_subscribe'])
        assert self.element_is_visible(SubscribeLocators.ERROR_MESSAGE)


    def subscribe_button_with_email(self, config):
        email = config['email']
        main_window = self.driver.current_window_handle

        self.element_is_visible(MainLocators.UPGRADE_BUTTON).click()
        self.element_is_visible(MainLocators.EMAIL_INPUT).send_keys(email)
            
        self.element_is_visible(MainLocators.SUBSCRIBE_BUTTON).click()

        self.window_hendler(main_window)

        assert self.driver.current_url.startswith(config['additional_url']['benhowdle_subscribe'])
        assert self.element_is_visible(SubscribeLocators.RETURN_BUTTON)
        

    def swagger_button(self, config):
        self.element_is_visible(MainLocators.SWAGGER).click()

        assert self.url_check(config['additional_url']['swagger_dock'])


    def sailsjs_button(self, config):
        self.element_is_visible(MainLocators.SAILSJS_BUTTON).click()

        assert self.url_check(config['additional_url']['sailsjs'])
        
    
    def designed_by(self, config):
        self.element_is_visible(MainLocators.DESIGNED_BY).click()

        assert self.url_check(config['additional_url']['benhowdle_resume'])
