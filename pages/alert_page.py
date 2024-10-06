from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.button import Button
from elements.label import Label


class AlertPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    JS_ALERT = (By.XPATH, '//button[@onclick="jsAlert()"]')
    JS_CONFIRM = (By.XPATH, '//button[@onclick="jsConfirm()"]')
    JS_PROMPT = (By.XPATH, '//button[@onclick="jsPrompt()"]')
    RESULT = (By.ID, 'result')

    def __init__(self, driver):
        unique_element = Label(driver, self.UNIQUE_ELEMENT)
        super().__init__(driver, unique_element)
        self.button_1 = Button(driver, self.JS_ALERT, description="Alert Page -> JS Alert -> Alert button")
        self.button_2 = Button(driver, self.JS_CONFIRM, description="Alert Page -> JS Confirm -> Confirm button")
        self.button_3 = Button(driver, self.JS_PROMPT, description="Alert Page ->  JS Prompt -> Prompt button")
        self.label = Label(driver, self.RESULT, description="Alert Page -> Action result")


    def click_on_js_alert(self):
        self.logger.info("Клик по кнопке JS Alert")
        self.button_1.click()

    def click_on_js_confirm(self):
        self.logger.info("Клик по кнопке JS Confirm")
        self.button_2.click()

    def click_on_js_prompt(self):
        self.logger.info("Клик по кнопке JS Prompt")
        self.button_3.click()

    def get_result_text(self):
        self.logger.info("Получение текста результата действия")
        self.label = Label(self.driver, self.RESULT, description="Alert Page -> Action result")
        result_text = self.label.get_text()
        self.logger.info(f"Текст результата: {result_text}")
        return result_text
    

