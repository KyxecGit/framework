from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from browser.factory import BrowserFactory
from utils.logger import Logger
from utils.config import DEFAULT_WAIT_TIME


class Browser:
    def __init__(self):
        self._driver = BrowserFactory.get_driver()
        self.wait = WebDriverWait(self._driver, DEFAULT_WAIT_TIME)
        self.logger = Logger.setup_logger()

    def get_driver(self):
        return self._driver

    def get(self, url):
        self.logger.info(f"Переход по адресу: {url}")
        self._driver.get(url)

    def close(self):
        self.logger.info("Закрытие текущей страницы")
        self._driver.close()

    def quit(self):
        self.logger.info("Закрытие браузера")
        self._driver.quit()

    def refresh(self):
        self.logger.info("Обновление текущей страницы")
        self._driver.refresh()

    def get_current_url(self):
        self.logger.info("Получение текущего URL")
        return self._driver.current_url

    def get_title(self):
        self.logger.info("Получение заголовка страницы")
        return self._driver.title
    
    def get_current_window_handle(self):
        self.logger.info("Получение идентификатора текущего окна")
        return self._driver.current_window_handle
    
    def get_page_source(self):
        self.logger.info("Получение исходного кода страницы")
        return self._driver.page_source
    
    def execute_script(self, script, *args):
        self.logger.info(f"Выполнение JavaScript: {script} с аргументами {args}")
        return self._driver.execute_script(script, *args)
    
    def switch_to_window(self, window_handle):
        self.logger.info("Переключение на другое окно")
        self._driver.switch_to.window(window_handle)

    def switch_to_iframe(self, iframe):
        self.logger.info(f"Переключение на iframe: {iframe}")
        self._driver.switch_to.frame(iframe)
    
    def switch_to_the_tab(self, current_window_handle):
        self.logger.info("Ожидание новой вкладки")
        
        self.wait.until(
            lambda driver: len(driver.window_handles) > 1
        )

        for handle in self._driver.window_handles:
            if handle != current_window_handle:
                self.logger.info(f"Переключение на вкладку: {handle}")
                self._driver.switch_to.window(handle)
                break


    def close_tab_by_title(self, title):
        self.logger.info(f"Закрытие вкладки с заголовком: {title}")
        for handle in self._driver.window_handles:
            self._driver.switch_to.window(handle)
            if self.get_title() == title:
                self.close()
                break

    def get_alert_text(self):
        self.logger.info("Получение текста алерта")
        return self.wait.until(EC.alert_is_present()).text
    
    def accept_alert(self):
        self.logger.info("Принятие алерта")
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def send_keys_to_alert(self, value):
        self.logger.info(f"Отправка значения: {value} в алерт")
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(value)

    def find_element(self, by, value):
        return self._driver.find_element(by, value)