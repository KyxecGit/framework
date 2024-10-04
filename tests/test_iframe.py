from pages.iframe_page import IframePage
from utils.logger import Logger  


class TestIframeNavigation:
    URL = "https://demoqa.com/alertsWindows"
    PARENT_TEXT = "Parent frame"
    CHILD_TEXT = "Child Iframe"


    def test_iframe_navigation(self, browser):
        self.logger = Logger.setup_logger(name='test_iframe_navigation')
        self.logger.info("Запуск теста навигации по iframe")
        browser.get(self.URL)

        self.iframe_page = IframePage(browser)
        self.iframe_page.wait_for_open()

        self.iframe_page.redirection_to_iframes_page()
        self.logger.info("Перешли на страницу с iframe")

        assert self.iframe_page.get_presence_of_title_located(), "Заголовок страницы отсутствует"

        parent_frame_element = self.iframe_page.get_presence_of_parent_frame_located()
        browser.switch_to_iframe(parent_frame_element)
        self.logger.info("Переключились на родительский iframe")

        actual_text = self.iframe_page.get_frame_text()
        assert actual_text == self.PARENT_TEXT, \
            f"Expected {self.PARENT_TEXT} in iframe, got {actual_text} instead"

        child_frame_element = self.iframe_page.get_presence_of_child_iframe_located()
        browser.switch_to_iframe(child_frame_element)
        self.logger.info("Переключились на дочерний iframe")

        actual_text = self.iframe_page.get_iframe_text()
        assert actual_text == self.CHILD_TEXT, \
            f"Expected {self.CHILD_TEXT} in iframe, got {actual_text} instead"
