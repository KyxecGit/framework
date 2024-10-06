from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.element import Element
from elements.label import Label

class ContentPage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')

    def __init__(self, driver):
        unique_element = Label(driver, self.UNIQUE_ELEMENT)
        super().__init__(driver, unique_element)


    def get_image_source(self, index):
        self.logger.info(f"Getting image source for image {index}")
        image = Element(self.driver, (By.XPATH,f'(//div[contains(@class, "large-2 columns")]/img)[{index}]'),
                       description=f"Dynamic content Page -> Image_{index}" )
        source = image.get_attribute('src')
        self.logger.info(f"Image {index} source: {source}")
        return source


    def get_images_sources(self):
        self.logger.info("Получение источников всех изображений")
        sources = [self.get_image_source(1), self.get_image_source(2), self.get_image_source(3)]
        self.logger.info(f"Источники изображений: {sources}")
        return sources
