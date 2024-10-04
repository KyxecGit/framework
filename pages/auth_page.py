from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.label import Label
from utils.logger import Logger


class AuthPage(BasePage):
    PAGE_TEXT = (By.XPATH, '//div[contains(@class, "example")]/p')

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(name='AuthPage')

    def get_page_text(self):
        self.logger.info("Получение текста на странице авторизации")
        self.label = Label(self.driver, self.PAGE_TEXT, description="Authorization Page -> Authorization text")
        page_text = self.label.get_text()
        self.logger.info(f"Текст страницы: {page_text}")
        return page_text
