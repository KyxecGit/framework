from selenium.webdriver.common.by import By
from elements.label import Label
from elements.slider import SliderElement
from .base_page import BasePage


class SliderPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    SLIDER = (By.XPATH, '//*[@type="range"]')
    SLIDER_VALUE = (By.ID, 'range')


    def __init__(self, driver):
        unique_element = Label(driver, self.UNIQUE_ELEMENT)
        super().__init__(driver, unique_element)
        self.slider = SliderElement(driver, self.SLIDER, description="Slider Page -> Slider")
        self.label = Label(driver, self.SLIDER_VALUE, description="Slider Page -> Slider Value")


    def move_slider(self, direction, value):
        self.logger.info(f"Перемещение слайдера: направление {direction}, значение {value}")
        self.slider.move(direction=direction, value=value)
        return self.slider.calculate_value(value)

    def get_slider_value(self):
        self.logger.info("Получение значения слайдера")
        real_value = float(self.label.get_text())
        self.logger.info(f"Текущее значение слайдера: {real_value}")
        return real_value
