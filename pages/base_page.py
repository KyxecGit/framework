from utils.logger import Logger

class BasePage:
    UNIQUE_ELEMENT = None


    def __init__(self, driver):
        self.driver = driver
        self.unique_element = None
        self.logger = Logger.setup_logger()

    def wait_for_open(self):
        self.unique_element.get_presence_of_element_located()