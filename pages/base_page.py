from utils.logger import Logger

class BasePage:
    def __init__(self, driver, unique_element):
        self.driver = driver
        self.unique_element = unique_element
        self.logger = Logger.setup_logger()

    def wait_for_open(self):
        self.logger.info("Wait to open")
        self.unique_element.get_presence_of_element_located()
