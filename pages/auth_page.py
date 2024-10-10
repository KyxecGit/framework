from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.label import Label


class AuthPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    PAGE_TEXT = (By.XPATH, '//div[contains(@class, "example")]/p')


    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(driver, self.UNIQUE_ELEMENT)
        self.label = Label(driver, self.PAGE_TEXT, description="Authorization Page -> Authorization text")


    def get_page_text(self):
        self.logger.info("Получение текста на странице авторизации")
        page_text = self.label.get_text()
        self.logger.info(f"Текст страницы: {page_text}")
        return page_text