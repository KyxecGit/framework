import pytest
from pages.scroll_page import ScrollPage
from utils.logger import Logger  
from utils.config import SCROLL_URL


class TestInfiniteScroll:
    logger = Logger.setup_logger()

    @pytest.mark.parametrize('target_count', [5])
    def test_infinite_scroll(self, browser, target_count):
        
        self.logger.info("Запуск теста прокрутки до заданного количества параграфов")
        browser.get(SCROLL_URL)

        self.infinite_scroll_page = ScrollPage(browser)
        self.infinite_scroll_page.wait_for_open()

        actual_paragraphs_count = self.infinite_scroll_page.scroll_to_paragraph_count(target_count)

        self.logger.info(f"Ожидаемое количество параграфов: {target_count}, фактическое количество: {actual_paragraphs_count}")
        
        assert actual_paragraphs_count == target_count, \
            f"Ожидалось {target_count}, но получено {actual_paragraphs_count}"