from pages.auth_page import AuthPage
from utils.logger import Logger 


class TestBasicAuth:
    URL = "https://{}:{}@the-internet.herokuapp.com/basic_auth"
    LOGIN = "admin"
    PASS = "admin"
    EXPECTED_AUTH_TEXT = "Congratulations! You must have the proper credentials."


    def test_basic_auth(self, browser):
        self.logger = Logger.setup_logger(name='test_basic_auth')
        self.logger.info("Запуск теста авторизации")
        browser.get(self.URL.format(self.LOGIN, self.PASS))

        self.auth_page = AuthPage(browser)
        self.auth_page.wait_for_open()

        page_text = self.auth_page.get_page_text()

        assert page_text == self.EXPECTED_AUTH_TEXT, \
            f"Требуемый текст {page_text} не соответствует {self.EXPECTED_AUTH_TEXT}"
