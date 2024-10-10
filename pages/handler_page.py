from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.button import Button
from elements.label import Label


class HandlerPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    BUTTON = (By.XPATH, '//div[contains(@class,"example")]//a')

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(driver, self.UNIQUE_ELEMENT)
        self.button = Button(driver, self.BUTTON, description="Handlers Page -> Redirection Button")


    def click_for_new_tab(self):
        self.logger.info("Клик по кнопке для открытия новой вкладки")
        self.button.click()
        self.logger.info("Кнопка для открытия новой вкладки успешно нажата.")