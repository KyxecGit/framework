import pytest
from pages.image_page import ImagePage
from utils.logger import Logger
from utils.config import IMAGE_URL


class TestUploadImage:
    logger = Logger.setup_logger()


    @pytest.mark.parametrize('path, image_name', [("C:\image.jpg", "image.jpg")])
    def test_upload_image(self, browser, path, image_name):
        
        self.logger.info("Запуск теста загрузки изображения")
        browser.get(IMAGE_URL)

        self.upload_image_page = ImagePage(browser)
        self.upload_image_page.wait_for_open()

        self.upload_image_page.upload_image(path)

        actual_name = self.upload_image_page.get_image_text()
        self.logger.info(f"Ожидаемое имя: {image_name}, фактическое имя: {actual_name}")
        assert actual_name == image_name, "Имя файла не отображается"

    @pytest.mark.parametrize('path, image_name', [("C:\image.jpg", "image.jpg")])
    def test_upload_image_dialog_window(self, browser, path, image_name):
        self.logger.info("Запуск теста загрузки изображения через диалоговое окно")
        browser.get(IMAGE_URL)

        self.upload_image_page = ImagePage(browser)
        self.upload_image_page.wait_for_open()

        self.upload_image_page.upload_image2(path)

        actual_name = self.upload_image_page.get_image_text2()
        self.logger.info(f"Ожидаемое имя: {image_name}, фактическое имя: {actual_name}")
        assert actual_name == image_name, "Имя файла не отображается"

        assert self.upload_image_page.presence_of_check_mark_located(), "Символ галочки не появился"
        self.logger.info("Символ галочки появился, тест завершен успешно")