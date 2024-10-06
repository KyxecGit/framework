import os
from pages.auth_page import AuthPage
from utils.logger import Logger 
from utils.config import AUTH_URL


class TestBasicAuth:
    LOGIN = os.getenv("LOGIN")
    PASS = os.getenv("PASS")
    EXPECTED_AUTH_TEXT = "Congratulations! You must have the proper credentials."
    logger = Logger.setup_logger()


    def test_basic_auth(self, browser):
        self.logger.info("Запуск теста авторизации")
        browser.get(AUTH_URL.format(self.LOGIN, self.PASS))

        self.auth_page = AuthPage(browser)
        self.auth_page.wait_for_open()

        page_text = self.auth_page.get_page_text()

        assert page_text == self.EXPECTED_AUTH_TEXT, \
            f"Требуемый текст {page_text} не соответствует {self.EXPECTED_AUTH_TEXT}"
