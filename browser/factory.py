from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from utils.config import CHROME_OPTIONS

class BrowserFactory:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument(CHROME_OPTIONS)  
        driver = Chrome(options=options)
        return driver