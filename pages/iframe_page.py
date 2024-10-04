from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.label import Label
from elements.element import Element
from utils.logger import Logger


class IframePage(BasePage):
    NESTED_FRAMES = (By.XPATH, "//span[text()='Nested Frames']")
    NESTED_FRAMES_TITLE = (By.XPATH, '//h1[contains(@class, "text-center")]')
    PARENT_FRAME = (By.ID, 'frame1')
    TEXT_INSIDE_PFRAME = (By.XPATH, '//body[normalize-space(.)="Parent frame"]')
    CHILD_IFRAME = (By.XPATH, '//iframe[@srcdoc]')
    TEXT_INSIDE_IFRAME = (By.XPATH, '//body[normalize-space(.)="Child Iframe"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.setup_logger(name='IframePage')

    def scroll_into_label_view(self):
        self.logger.info("Прокрутка к метке 'Nested Frames'")
        self.label = Label(self.driver, self.NESTED_FRAMES, description="Main Page -> Nested Frames label")
        self.label.scroll_into_view()
        self.logger.info("Метка 'Nested Frames' успешно прокручена в видимую область.")

    def click_for_redirection(self):
        self.logger.info("Клик по метке 'Nested Frames' для редирекции")
        self.label = Element(self.driver, self.NESTED_FRAMES, description="Main Page -> Nested Frames button")
        self.label.click()
        self.logger.info("Кнопка 'Nested Frames' успешно нажата для редирекции.")

    def redirection_to_iframes_page(self):
        self.logger.info("Редирекция на страницу фреймов")
        self.scroll_into_label_view()
        self.click_for_redirection()
        self.logger.info("Успешная редирекция на страницу фреймов.")

    def get_presence_of_title_located(self):
        self.logger.info("Получение заголовка на странице фреймов")
        self.title = Label(self.driver, self.NESTED_FRAMES_TITLE, description="Frames Page -> Parent title")
        return self.title.get_presence_of_element_located()

    def get_presence_of_parent_frame_located(self):
        self.logger.info("Проверка наличия родительского фрейма")
        self.parent_frame = Element(self.driver, self.PARENT_FRAME, description="Frames Page -> Parent frame")
        return self.parent_frame.get_presence_of_element_located()

    def get_frame_text(self):
        self.logger.info("Получение текста из родительского фрейма")
        self.label_frame = Label(self.driver, self.TEXT_INSIDE_PFRAME, description="Frame Page -> Parent Frame text")
        return self.label_frame.get_text()

    def get_presence_of_child_iframe_located(self):
        self.logger.info("Проверка наличия дочернего фрейма")
        self.child_iframe = Element(self.driver, self.CHILD_IFRAME, description="Frames Page -> Child iframe")
        return self.child_iframe.get_presence_of_element_located()

    def get_iframe_text(self):
        self.logger.info("Получение текста из дочернего фрейма")
        self.label_iframe = Label(self.driver, self.TEXT_INSIDE_IFRAME, description="Frames Page -> Child Frame text")
        return self.label_iframe.get_text()
