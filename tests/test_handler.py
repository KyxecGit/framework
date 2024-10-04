from pages.handler_page import HandlerPage
from utils.logger import Logger  


class TestWindowHandler:
    URL = "https://the-internet.herokuapp.com/windows"
    NEW_WINDOW_TITLE = "New Window"


    def test_open_new_window(self, browser):
        self.logger = Logger.setup_logger(name='test_window_handler')
        self.logger.info("Запуск теста открытия нового окна")
        browser.get(self.URL)

        self.handlers_page = HandlerPage(browser)
        self.handlers_page.wait_for_open()

        main_window = browser.get_current_window_handle()
        self.logger.info("Главное окно захвачено: %s", main_window)

        self.handlers_page.click_for_new_tab()
        self.logger.info("Кликнули для открытия новой вкладки")

        browser.switch_to_the_tab(main_window)

        actual_title = browser.get_title()
        self.logger.info("Фактический заголовок окна: %s", actual_title)

        assert actual_title == self.NEW_WINDOW_TITLE, \
            f"Не удалось открыть страницу {self.NEW_WINDOW_TITLE}"

        browser.switch_to_window(main_window)
        self.handlers_page.wait_for_open()

        self.handlers_page.click_for_new_tab()
        self.logger.info("Кликнули для открытия новой вкладки")

        browser.switch_to_the_tab(main_window)

        actual_title = browser.get_title()
        self.logger.info("Фактический заголовок окна: %s", actual_title)
        assert actual_title == self.NEW_WINDOW_TITLE, \
            f"Не удалось открыть страницу {self.NEW_WINDOW_TITLE}"

        browser.switch_to_window(main_window)
        self.handlers_page.wait_for_open()

        browser.close_tab_by_title(self.NEW_WINDOW_TITLE)
        self.logger.info("Закрыли вкладку с заголовком: %s", self.NEW_WINDOW_TITLE)

        browser.close_tab_by_title(self.NEW_WINDOW_TITLE)
        self.logger.info("Закрыли вкладку с заголовком: %s", self.NEW_WINDOW_TITLE)
