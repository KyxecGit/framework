from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class BrowserFactory:

    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--window-size=1920,1080")  
        driver = Chrome(options=options)
        return driver