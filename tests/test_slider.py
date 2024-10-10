import random
import pytest
from pages.slider_page import SliderPage
from utils.logger import Logger
from utils.config import SLIDER_URL


class TestSliderActions:
    MIN_SLIDER_VALUE = 0
    MAX_SLIDER_VALUE = 8
    logger = Logger.setup_logger()


    @pytest.mark.parametrize("slider_direction", ["right"])
    def test_slider_movement(self, browser, slider_direction):
        self.logger.info("Запуск теста перемещения слайдера")
        browser.get(SLIDER_URL)

        self.actions_page = SliderPage(browser)
        self.actions_page.wait_for_open()
        slider_value = random.randint(self.MIN_SLIDER_VALUE, self.MAX_SLIDER_VALUE)
        expected_result = self.actions_page.move_slider(direction=slider_direction, value=slider_value)

        actual_result = self.actions_page.get_slider_value()

        self.logger.info(f"Ожидаемое значение: {expected_result}, фактическое значение: {actual_result}")

        assert actual_result == expected_result, \
            f"Слайдер не переместился на указанное значение {expected_result}, вместо этого переместился на {actual_result}"
