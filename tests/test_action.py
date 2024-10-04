import pytest
from pages.action_page import ActionPage
from utils.logger import Logger


class TestSliderAndHoverActions:
    URL = "https://the-internet.herokuapp.com/horizontal_slider"
    URL2 = "https://the-internet.herokuapp.com/hovers"


    @pytest.mark.parametrize("slider_value, slider_direction", [(8, "right")])
    def test_slider_movement(self, browser, slider_value, slider_direction):
        self.logger = Logger.setup_logger(name='test_slider')
        self.logger.info("Запуск теста перемещения слайдера")
        browser.get(self.URL)

        self.actions_page = ActionPage(browser)
        self.actions_page.wait_for_open()

        self.actions_page.move_slider(direction=slider_direction, value=slider_value)

        expected_result = 0.5 * slider_value
        actual_result = self.actions_page.get_slider_value()

        self.logger.info(f"Ожидаемое значение: {expected_result}, фактическое значение: {actual_result}")

        assert actual_result == expected_result, \
            f"Слайдер не переместился на указанное значение {expected_result}, вместо этого переместился на {actual_result}"

    @pytest.mark.parametrize("figure_index, expected_username, expected_link", [
        (1, "name: user1", "/users/1"),
        (2, "name: user2", "/users/2"),
        (3, "name: user3", "/users/3")
    ])
    def test_hover_and_click_profile(self, browser, figure_index, expected_username, expected_link):
        self.logger = Logger.setup_logger(name='test_hover')
        self.logger.info("Запуск теста наведения на фигуру")
        browser.get(self.URL2)

        self.hovers_page = ActionPage(browser)
        self.hovers_page.wait_for_open()

        self.hovers_page.hover_over_figure(figure_index)
        actual_text = self.hovers_page.get_caption_text(figure_index)

        self.logger.info(f"Ожидаемое имя: {expected_username}, фактическое имя: {actual_text}")
        assert actual_text == expected_username, f"Требуемый текст {expected_username} не совпадает с полученным {actual_text}"

        self.hovers_page.click_profile_label(figure_index)
        current_url = browser.get_current_url()
        assert current_url.endswith(expected_link), f"Текущий URL {current_url} не соответствует {expected_link}"
