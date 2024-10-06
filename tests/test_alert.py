import pytest
from pages.alert_page import AlertPage
from utils.logger import Logger  
from utils.config import ALERT_URL


class TestJavaScriptAlerts:
    JS_ALERT_TEXT = "I am a JS Alert"
    JS_CONFIRM_TEXT = "I am a JS Confirm"
    JS_PROMPT_TEXT = "I am a JS prompt"
    RESULT_ALERT_TEXT = "You successfully clicked an alert"
    RESULT_CONFIRM_TEXT = "You clicked: Ok"
    logger = Logger.setup_logger()


    def test_js_alert(self, browser):
        self.logger.info("Запуск теста JavaScript Alert")
        browser.get(ALERT_URL)

        self.alert_page = AlertPage(browser)
        self.alert_page.wait_for_open()

        self.alert_page.click_on_js_alert()

        actual_result_text = browser.get_alert_text()
        assert actual_result_text == self.JS_ALERT_TEXT, \
            f"Требуемый текст {actual_result_text} не соответствует {self.RESULT_ALERT_TEXT}"
        browser.accept_alert()

        actual_result_text = self.alert_page.get_result_text()
        assert actual_result_text == self.RESULT_ALERT_TEXT, \
            f"Требуемый текст {actual_result_text} не соответствует {self.RESULT_ALERT_TEXT}"

    def test_js_confirm(self, browser):
        self.logger.info("Запуск теста JavaScript Confirm")
        browser.get(ALERT_URL)

        self.alert_page = AlertPage(browser)
        self.alert_page.wait_for_open()

        self.alert_page.click_on_js_confirm()

        actual_result_text = browser.get_alert_text()
        assert actual_result_text == self.JS_CONFIRM_TEXT, \
            f"Требуемый текст {actual_result_text} не соответствует {self.JS_CONFIRM_TEXT}"
        browser.accept_alert()

        actual_result_text = self.alert_page.get_result_text()
        assert actual_result_text == self.RESULT_CONFIRM_TEXT, \
            f"Требуемый текст {actual_result_text} не соответствует {self.RESULT_CONFIRM_TEXT}"

    @pytest.mark.parametrize("input_word, expected_result_text", [("word", "You entered: word")])
    def test_js_prompt(self, browser, input_word, expected_result_text):
        self.logger.info("Запуск теста JavaScript Prompt")
        browser.get(ALERT_URL)

        self.alert_page = AlertPage(browser)
        self.alert_page.wait_for_open()

        self.alert_page.click_on_js_prompt()

        actual_result_text = browser.get_alert_text()
        assert actual_result_text == self.JS_PROMPT_TEXT, \
            f"Требуемый текст {actual_result_text} не соответствует {self.JS_PROMPT_TEXT}"
        browser.send_keys_to_alert(input_word)
        browser.accept_alert()

        actual_result_text = self.alert_page.get_result_text()
        assert actual_result_text == expected_result_text, \
            f"Требуемый текст {actual_result_text} не соответствует {expected_result_text}"
