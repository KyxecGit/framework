from pages.content_page import ContentPage
from utils.logger import Logger  


class TestDynamicContent:
    URL = "https://the-internet.herokuapp.com/dynamic_content"


    def test_dynamic_content(self, browser):
        self.logger = Logger.setup_logger(name='test_dynamic_content')
        self.logger.info("Запуск теста динамического контента")
        browser.get(self.URL)

        self.dynamic_content_page = ContentPage(browser)
        self.dynamic_content_page.wait_for_open()

        image_sources = self.dynamic_content_page.get_images_sources()

        while len(set(image_sources)) == 3:
            self.logger.info("Все три изображения совпадают. Обновление страницы.")
            browser.refresh()
            image_sources = self.dynamic_content_page.get_images_sources()

        image_1 = image_sources[0]
        image_2 = image_sources[1]
        image_3 = image_sources[2]

        assert image_1 == image_2 or image_1 == image_3 or image_2 == image_3, \
            "Изображения не совпадают"
