import allure

from pages.main_page import MainPage


class TestMainPage:

    @allure.severity('normal')
    def test_subscribe_button_with_email(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.subscribe_button_with_email(config)
    
    @allure.severity('normal')
    def test_subscribe_button_without_email(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.subscribe_button_without_email(config)
    
    @allure.severity('trivial')
    def test_heroku_button(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.heroku_button(config)


    def test_top_support_button(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.top_support_button()

    @allure.severity('critical')
    def test_main_support_button_first_method(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.main_support_button_first_method(config)

    @allure.severity('critical')
    def test_main_support_button_second_method(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.main_support_button_second_method(config)

    @allure.severity('critical')
    def test_upgrade_button(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.upgrade_button()

    @allure.severity('trivial')
    def test_swagger_button(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.swagger_button(config)

    @allure.severity('trivial')
    def test_sailsjs_button(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.sailsjs_button(config)

    @allure.severity('trivial')
    def test_designed_by(self, driver, config):
        main_page = MainPage(driver, config['main_url'])
        main_page.open()

        main_page.designed_by(config)