from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger


class BaseElement:
    def __init__(self, driver, locator, description=None):
        self.driver = driver.get_driver()
        self.locator = locator
        self.description = description
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)
        self.logger = Logger.setup_logger(name='element')

    def get_presence_of_element_located(self):
        self.logger.info(f"{self.description}: ожидание присутствия элемента")
        return self.wait.until(EC.presence_of_element_located(self.locator))
    
    def visibility_located(self):
        self.logger.info(f"Ожидание видимости элемента с локатором: {self.locator}")
        return self.wait.until(EC.visibility_of_element_located(self.locator))

    def get_text(self):
        self.logger.info(f"{self.description}: получение текста элемента")
        return self.get_presence_of_element_located().text
    
    def click(self):
        self.logger.info(f"{self.description}: клик по элементу")
        element = self.wait.until(EC.element_to_be_clickable(self.locator))
        element.click()

    def right_click(self):
        self.logger.info(f"{self.description}: правый клик")
        element = self.wait.until(EC.element_to_be_clickable(self.locator))
        self.action_chains.context_click(element).perform()

    def hover_over_element(self):
        self.logger.info(f"{self.description}: наведение на элемент")
        element = self.visibility_located()
        self.action_chains.move_to_element(element).perform()

    def scroll_into_view(self):
        self.logger.info(f"{self.description}: прокрутка к элементу")
        element = self.get_presence_of_element_located()
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_attribute(self, attribute):
        self.logger.info(f"{self.description}: получение атрибута '{attribute}' у элемента")
        return self.get_presence_of_element_located().get_attribute(attribute)
