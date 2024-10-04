from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.element import Element
from utils.logger import Logger


class ContentPage(BasePage):
    IMG_1 = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img)[1]')
    IMG_2 = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img)[2]')
    IMG_3 = (By.XPATH, '(//div[contains(@class, "large-2 columns")]/img)[3]')

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(name='ContentPage')

    def get_image_1_source(self):
        self.logger.info("Получение источника изображения 1")
        image_1 = Element(self.driver, self.IMG_1, description="Dynamic content Page -> Image_1")
        source = image_1.get_attribute('src')
        self.logger.info(f"Источник изображения 1: {source}")
        return source

    def get_image_2_source(self):
        self.logger.info("Получение источника изображения 2")
        image_2 = Element(self.driver, self.IMG_2, description="Dynamic content Page -> Image_2")
        source = image_2.get_attribute('src')
        self.logger.info(f"Источник изображения 2: {source}")
        return source

    def get_image_3_source(self):
        self.logger.info("Получение источника изображения 3")
        image_3 = Element(self.driver, self.IMG_3, description="Dynamic content Page -> Image_3")
        source = image_3.get_attribute('src')
        self.logger.info(f"Источник изображения 3: {source}")
        return source

    def get_images_sources(self):
        self.logger.info("Получение источников всех изображений")
        sources = [self.get_image_1_source(), self.get_image_2_source(), self.get_image_3_source()]
        self.logger.info(f"Источники изображений: {sources}")
        return sources
