from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.element import Element
from elements.label import Label

class ContentPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    IMAGE_TEMPLATE = '(//div[contains(@class, "large-2 columns")]//img)[{}]'

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(self.driver, self.UNIQUE_ELEMENT)

    def get_image_source(self, index):
        self.logger.info(f"Получение источника изображения с индексом {index}")
        image_locator = (By.XPATH, self.IMAGE_TEMPLATE.format(index))
        image = Element(self.driver, image_locator, description=f"Dynamic content Page -> Image_{index}")
        source = image.get_attribute('src')
        return source

    def get_images_sources(self):
        self.logger.info("Получение источников всех изображений")
        sources = [self.get_image_source(i) for i in range(1, 4)]  
        self.logger.info(f"Источники изображений: {sources}")
        return sources