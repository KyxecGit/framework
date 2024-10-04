from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.button import Button
from elements.label import Label
from elements.element import Element
from utils.logger import Logger


class AlertPage(BasePage):
    JS_ALERT = (By.XPATH, '//button[@onclick="jsAlert()"]')
    JS_CONFIRM = (By.XPATH, '//button[@onclick="jsConfirm()"]')
    JS_PROMPT = (By.XPATH, '//button[@onclick="jsPrompt()"]')
    CONTEXT_MENU = (By.ID, 'hot-spot')
    RESULT = (By.ID, 'result')

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(name='AlertPage')

    def click_on_js_alert(self):
        self.logger.info("Клик по кнопке JS Alert")
        self.button = Button(self.driver, self.JS_ALERT, description="Alert Page -> JS Alert -> Alert button")
        self.button.click()

    def click_on_js_confirm(self):
        self.logger.info("Клик по кнопке JS Confirm")
        self.button = Button(self.driver, self.JS_CONFIRM, description="Alert Page -> JS Confirm -> Confirm button")
        self.button.click()

    def click_on_js_prompt(self):
        self.logger.info("Клик по кнопке JS Prompt")
        self.button = Button(self.driver, self.JS_PROMPT, description="Alert Page -> JS Prompt -> Prompt button")
        self.button.click()

    def get_result_text(self):
        self.logger.info("Получение текста результата действия")
        self.label = Label(self.driver, self.RESULT, description="Alert Page -> Action result")
        result_text = self.label.get_text()
        self.logger.info(f"Текст результата: {result_text}")
        return result_text
    
    def right_click_on_window(self):
        self.logger.info("Правый клик на окне контекстного меню")
        self.element = Element(self.driver, self.CONTEXT_MENU, description="Context Menu Page -> Window")
        self.element.right_click()
