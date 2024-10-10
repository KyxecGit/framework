from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.label import Label
from elements.element import Element


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    CONTEXT_MENU = (By.ID, 'hot-spot')

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(driver, self.UNIQUE_ELEMENT)
        self.element = Element(driver, self.CONTEXT_MENU, description="Context Menu Page -> Window")


    def right_click_on_window(self):
        self.logger.info("Правый клик на окне контекстного меню")
        self.element.right_click()