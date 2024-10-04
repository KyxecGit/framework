from selenium.webdriver import Keys
from elements.base_element import BaseElement


class SliderElement(BaseElement):
    def move(self, direction, value):
        slider = self.get_presence_of_element_located()
        if direction == 'right':
            slider.send_keys(Keys.ARROW_RIGHT * value)
        elif direction == 'left':
            slider.send_keys(Keys.ARROW_LEFT * value)