from enum import Enum
from selenium.webdriver import Keys
from elements.base_element import BaseElement


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'


class SliderElement(BaseElement):
    COEFFICIENT = 0.5

    def move(self, direction, value):
        slider = self.get_presence_of_element_located()
        if direction == Direction.RIGHT.value:
            slider.send_keys(Keys.ARROW_RIGHT * value)
        elif direction == Direction.LEFT.value:
            slider.send_keys(Keys.ARROW_LEFT * value)

    def _calculate_value(self, slider_value):
        return self.COEFFICIENT * slider_value