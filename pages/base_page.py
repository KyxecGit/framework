from utils.logger import Logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.setup_logger(name='BasePage')

    def wait_for_open(self):
        self.logger.info("Ожидание полной загрузки страницы")
        is_ready = self.driver.execute_script("return document.readyState") == "complete"
        if is_ready:
            self.logger.info("Страница загружена полностью")
        else:
            self.logger.warning("Страница не загружена полностью")
        return is_ready
