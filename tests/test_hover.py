import pytest
from pages.hover_page import HoverPage
from utils.logger import Logger
from utils.config import HOVER_URL

class TestHoverActions:
    logger = Logger.setup_logger()


    @pytest.mark.parametrize("figure_index, expected_username, expected_link", [
        (1, "name: user1", "/users/1"),
        (2, "name: user2", "/users/2"),
        (3, "name: user3", "/users/3")
    ])
    def test_hover_and_click_profile(self, browser, figure_index, expected_username, expected_link):
        self.logger.info("Запуск теста наведения на фигуру")
        browser.get(HOVER_URL)

        self.hovers_page = HoverPage(browser)
        self.hovers_page.wait_for_open()

        self.hovers_page.hover_over_figure(figure_index)
        actual_text = self.hovers_page.get_caption_text(figure_index)

        self.logger.info(f"Ожидаемое имя: {expected_username}, фактическое имя: {actual_text}")
        assert actual_text == expected_username, f"Требуемый текст {expected_username} не совпадает с полученным {actual_text}"

        self.hovers_page.click_profile_label(figure_index)
        current_url = browser.get_current_url()
        assert current_url.endswith(expected_link), f"Текущий URL {current_url} не соответствует {expected_link}"
