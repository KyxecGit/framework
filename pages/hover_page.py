from selenium.webdriver.common.by import By
from elements.element import Element
from elements.label import Label
from .base_page import BasePage


class HoverPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    FIGURE_TEMPLATE = '(//div[contains(@class,"figure")])[{}]'
    CAPTION_TEMPLATE = '(//div[contains(@class,"figcaption")])[{}]/h5'
    LABEL_TEMPLATE = '(//div[contains(@class,"figcaption")])[{}]//a'


    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(driver, self.UNIQUE_ELEMENT)


    def click_profile_label(self, index):
        self.logger.info(f"Клик по профилю с индексом {index}")
        profile_label_template = (By.XPATH, self.LABEL_TEMPLATE.format(index))
        profile_label = Label(self.driver, profile_label_template, description="Hovers Page -> Profile Template")
        profile_label.click()

    def get_caption_text(self, index):
        self.logger.info(f"Получение текста подписи для элемента с индексом {index}")
        
        caption_locator = (By.XPATH, self.CAPTION_TEMPLATE.format(index))
        caption = Label(self.driver, caption_locator, description="Hovers Page -> Caption Template")
        
        caption_text = caption.get_text()
        self.logger.info(f"Текст подписи: {caption_text}")
        return caption_text


    def hover_over_figure(self, index):
        self.logger.info(f"Наведение на фигуру с индексом {index}")
        figure_template = (By.XPATH, self.FIGURE_TEMPLATE.format(index))
        figure = Element(self.driver, figure_template, description="Hovers Page -> Figure Template")
        figure.hover_over_element()