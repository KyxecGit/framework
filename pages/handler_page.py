from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.button import Button
from utils.logger import Logger


class HandlerPage(BasePage):
    BUTTON = (By.XPATH, '//div[contains(@class,"example")]//a')

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(name='HandlerPage')

    def click_for_new_tab(self):
        self.logger.info("Клик по кнопке для открытия новой вкладки")
        self.button = Button(self.driver, self.BUTTON, description="Handlers Page -> Redirection Button")
        self.button.click()
        self.logger.info("Кнопка для открытия новой вкладки успешно нажата.")
