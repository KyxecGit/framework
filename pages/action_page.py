from selenium.webdriver.common.by import By
from elements.element import Element
from elements.label import Label
from elements.slider import SliderElement
from .base_page import BasePage
from utils.logger import Logger


class ActionPage(BasePage):
    SLIDER = (By.XPATH, '//*[@type="range"]')
    SLIDER_VALUE = (By.ID, 'range')
    FIGURE_TEMPLATE = '(//div[contains(@class,"figure")])[{}]'
    CAPTION_TEMPLATE = '(//div[contains(@class,"figcaption")])[{}]/h5'
    LABEL_TEMPLATE = '(//div[contains(@class,"figcaption")])[{}]//a'

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(name='ActionPage')

    def move_slider(self, direction, value):
        self.logger.info(f"Перемещение слайдера: направление {direction}, значение {value}")
        self.slider = SliderElement(self.driver, self.SLIDER, description="Slider Page -> Slider")
        self.slider.move(direction=direction, value=value)

    def get_slider_value(self):
        self.logger.info("Получение значения слайдера")
        self.label = Label(self.driver, self.SLIDER_VALUE, description="Slider Page -> Slider Value")
        real_value = float(self.label.get_text())
        self.logger.info(f"Текущее значение слайдера: {real_value}")
        return real_value

    def click_profile_label(self, index):
        self.logger.info(f"Клик по профилю с индексом {index}")
        profile_label_template = (By.XPATH, self.LABEL_TEMPLATE.format(index))
        profile_label = Label(self.driver, profile_label_template, description="Hovers Page -> Profile Template")
        profile_label.click()

    def get_caption_text(self, index):
        self.logger.info(f"Получение текста подписи для элемента с индексом {index}")
        caption_template = (By.XPATH, self.CAPTION_TEMPLATE.format(index))
        caption = Label(self.driver, caption_template, description="Hovers Page -> Caption Template")
        caption_text = caption.get_text()
        self.logger.info(f"Текст подписи: {caption_text}")
        return caption_text

    def hover_over_figure(self, index):
        self.logger.info(f"Наведение на фигуру с индексом {index}")
        figure_template = (By.XPATH, self.FIGURE_TEMPLATE.format(index))
        figure = Element(self.driver, figure_template, description="Hovers Page -> Figure Template")
        figure.hover_over_element()
