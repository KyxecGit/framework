from pages.content_page import ContentPage
from utils.logger import Logger  
from utils.config import CONTENT_URL


class TestDynamicContent:
    logger = Logger.setup_logger()


    def test_dynamic_content(self, browser):
        self.logger.info("Запуск теста динамического контента")
        browser.get(CONTENT_URL)

        self.dynamic_content_page = ContentPage(browser)
        self.dynamic_content_page.wait_for_open()

        image_sources = self.dynamic_content_page.get_images_sources()

        while len(set(image_sources)) == 3:
            self.logger.info("Все три изображения совпадают. Обновление страницы.")
            browser.refresh()
            image_sources = self.dynamic_content_page.get_images_sources()

        image_1, image_2, image_3 = image_sources

        assert image_1 == image_2 or image_1 == image_3 or image_2 == image_3, \
            "Изображения не совпадают"
