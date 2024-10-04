from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.button import Button
from elements.label import Label
from elements.input import Input
from elements.element import Element
from utils.logger import Logger

class ImagePage(BasePage):
    IMG_BUTTON = (By.ID, 'file-upload')
    IMG_BUTTON2 = (By.ID, 'drag-drop-upload')
    UPLOAD_IMG_BUTTON = (By.ID, 'file-submit')
    UPLOADED_FILE_TEXT = (By.ID, 'uploaded-files')
    UPLOADED_FILE_TEXT2 = (By.XPATH, '(//div[contains(@class, "dz-filename")])[1]//span')
    CHECK_MARK_SYMBOL = (By.XPATH, '(//div[contains(@class, "dz-success-mark")])[2]//span')

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(name='image_page')

    def send_keys(self, image):
        self.logger.info(f"Отправка изображения: {image}")
        self.input = Input(self.driver, self.IMG_BUTTON, description="Страница загрузки изображения -> Кнопка загрузки")
        self.input.send_keys(image)

    def click_to_submit_image(self):
        self.logger.info("Нажатие на кнопку загрузки изображения")
        self.button = Button(self.driver, self.UPLOAD_IMG_BUTTON, description="Страница загрузки изображения -> Кнопка загрузки")
        self.button.click()

    def get_image_text(self):
        self.logger.info("Получение текста загруженного файла")
        self.label = Label(self.driver, self.UPLOADED_FILE_TEXT, description="Страница загрузки изображения -> Загруженный файл")
        return self.label.get_text()    

    def upload_image(self, image):
        self.send_keys(image)
        self.click_to_submit_image()

    def click_to_submit_image2(self):
        self.logger.info("Нажатие на кнопку загрузки изображения через диалоговое окно")
        self.web_element = Element(self.driver, self.IMG_BUTTON2, description="Страница загрузки изображения -> Окно загрузки")
        self.web_element.click()

    def upload_image2(self, path):
        self.logger.info("Загрузка изображения через диалоговое окно")
        self.click_to_submit_image()

    def get_image_text2(self):
        self.logger.info("Получение текста загруженного файла из диалогового окна")
        self.label = Label(self.driver, self.UPLOADED_FILE_TEXT2, description="Страница загрузки изображения -> Загруженный файл")
        return self.label.get_text()

    def presence_of_check_mark_located(self):
        self.logger.info("Проверка наличия символа галочки")
        self.web_element_2 = Element(self.driver, self.CHECK_MARK_SYMBOL, description="Страница загрузки изображения -> Символ галочки")
        return self.web_element_2.get_presence_of_element_located()
