import pytest
from pages.scroll_page import ScrollPage
from utils.logger import Logger  


class TestInfiniteScroll:
    URL = "https://the-internet.herokuapp.com/infinite_scroll"


    @pytest.mark.parametrize('target_count', [5])
    def test_infinite_scroll(self, browser, target_count):
        self.logger = Logger.setup_logger(name='test_infinite_scroll')
        self.logger.info("Запуск теста прокрутки до заданного количества параграфов")
        browser.get(self.URL)

        self.infinite_scroll_page = ScrollPage(browser)
        self.infinite_scroll_page.wait_for_open()

        # Вызов метода для прокрутки
        actual_paragraphs_count = self.infinite_scroll_page.scroll_to_paragraph_count(target_count)

        self.logger.info(f"Ожидаемое количество параграфов: {target_count}, фактическое количество: {actual_paragraphs_count}")
        
        assert actual_paragraphs_count == target_count, \
            f"Ожидалось {target_count}, но получено {actual_paragraphs_count}"
