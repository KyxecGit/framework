import time
import pyautogui
from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.button import Button
from elements.label import Label
from elements.input import Input
from elements.element import Element

class ImagePage(BasePage):
    UNIQUE_ELEMENT = (By.ID, 'page-footer')
    IMG_BUTTON = (By.ID, 'file-upload')
    IMG_BUTTON2 = (By.ID, 'drag-drop-upload')
    UPLOAD_IMG_BUTTON = (By.ID, 'file-submit')
    UPLOADED_FILE_TEXT = (By.ID, 'uploaded-files')
    UPLOADED_FILE_TEXT2 = (By.XPATH, '(//div[contains(@class, "dz-filename")])[1]//span')
    CHECK_MARK_SYMBOL = (By.XPATH, '//*[@id="drag-drop-upload"]/div/div[2]/span')

    def __init__(self, driver):
        unique_element = Label(driver, self.UNIQUE_ELEMENT)
        super().__init__(driver, unique_element)
        self.button = Button(driver, self.UPLOAD_IMG_BUTTON, description="Upload Image Page -> Upload Button")
        self.input = Input(driver, self.IMG_BUTTON, description="Upload Image Page -> Unload Button")
        self.label = Label(driver, self.UPLOADED_FILE_TEXT, description="Upload Image Page -> Uploaded file")
        self.label2 = Label(driver, self.UPLOADED_FILE_TEXT2, description="Upload Image Page -> Uploaded file")
        self.element_1 = Element(driver, self.IMG_BUTTON2, description="Image Upload Page -> Upload Window")
        self.element_2 = Element(driver, self.CHECK_MARK_SYMBOL, description="Image Upload Page -> Check mark")


    def send_keys(self, image):
        self.logger.info(f"Отправка изображения: {image}")
        self.input.send_keys(image)

    def click_to_submit_image(self):
        self.logger.info("Нажатие на кнопку загрузки изображения")
        self.button.click()

    def get_image_text(self):
        self.logger.info("Получение текста загруженного файла")
        return self.label.get_text()    

    def upload_image(self, image):
        self.send_keys(image)
        self.click_to_submit_image()

    #походу как то криво реализовал но работает
    def upload_image2(self, image):
        self.logger.info("Загрузка изображения через диалоговое окно")
        self.element_1.click()
        time.sleep(2)
        pyautogui.write(image)
        pyautogui.press('enter')

    def get_image_text2(self):
        self.logger.info("Получение текста загруженного файла из диалогового окна")
        return self.label2.get_text()

    def presence_of_check_mark_located(self):
        self.logger.info("Проверка наличия символа галочки")
        return self.element_2.get_presence_of_element_located()
