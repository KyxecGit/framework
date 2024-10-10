from pages.menu_page import ContextMenuPage
from utils.logger import Logger  
from utils.config import CM_URL


class TestContextMenu:
    RESULT_CONTEXT_MENU_TEXT = "You selected a context menu"
    logger = Logger.setup_logger()


    def test_context_menu_alert(self, browser):
        self.logger.info("Запуск теста контекстного меню")
        browser.get(CM_URL)

        self.alert_page = ContextMenuPage(browser)
        self.alert_page.wait_for_open()

        self.alert_page.right_click_on_window()

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == self.RESULT_CONTEXT_MENU_TEXT, \
            f"Требуемый текст {actual_alert_text} не соответствует {self.RESULT_CONTEXT_MENU_TEXT}"
        browser.accept_alert()