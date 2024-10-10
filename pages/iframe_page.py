from selenium.webdriver.common.by import By
from .base_page import BasePage
from elements.label import Label
from elements.element import Element


class IframePage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, "//footer")
    NESTED_FRAMES = (By.XPATH, "//span[text()='Nested Frames']")
    NESTED_FRAMES_TITLE = (By.XPATH, '//h1[contains(@class, "text-center")]')
    PARENT_FRAME = (By.ID, 'frame1')
    TEXT_INSIDE_PFRAME = (By.XPATH, '//body[normalize-space(.)="Parent frame"]')
    CHILD_IFRAME = (By.XPATH, '//iframe[@srcdoc]')
    TEXT_INSIDE_IFRAME = (By.XPATH, '//body[normalize-space(.)="Child Iframe"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(driver, self.UNIQUE_ELEMENT)
        self.label = Label(driver, self.NESTED_FRAMES, description="Main Page -> Redirection button")
        self.title = Label(driver, self.NESTED_FRAMES_TITLE, description="Frames Page -> Parent title")
        self.parent_frame = Element(driver, self.PARENT_FRAME, description="Frames Page -> Parent frame")
        self.label_frame = Label(driver, self.TEXT_INSIDE_PFRAME, description="Frame Page -> Parent Frame text")
        self.child_iframe = Element(driver, self.CHILD_IFRAME, description="Frames Page -> Child iframe")
        self.label_iframe = Label(driver, self.TEXT_INSIDE_IFRAME, description="Frames Page -> Child Frame text")


    def scroll_into_label_view(self):
        self.logger.info("Прокрутка к метке 'Nested Frames'")
        self.label.scroll_into_view()
        self.logger.info("Метка 'Nested Frames' успешно прокручена в видимую область.")

    def click_for_redirection(self):
        self.logger.info("Клик по метке 'Nested Frames' для редирекции")
        self.label.click()
        self.logger.info("Кнопка 'Nested Frames' успешно нажата для редирекции.")

    def redirection_to_iframes_page(self):
        self.logger.info("Редирекция на страницу фреймов")
        self.scroll_into_label_view()
        self.click_for_redirection()
        self.logger.info("Успешная редирекция на страницу фреймов.")

    def get_presence_of_title_located(self):
        self.logger.info("Получение заголовка на странице фреймов")
        return self.title.get_presence_of_element_located()

    def get_presence_of_parent_frame_located(self):
        self.logger.info("Проверка наличия родительского фрейма")
        return self.parent_frame.get_presence_of_element_located()

    def get_frame_text(self):
        self.logger.info("Получение текста из родительского фрейма")
        return self.label_frame.get_text()

    def get_presence_of_child_iframe_located(self):
        self.logger.info("Проверка наличия дочернего фрейма")
        return self.child_iframe.get_presence_of_element_located()

    def get_iframe_text(self):
        self.logger.info("Получение текста из дочернего фрейма")
        return self.label_iframe.get_text()