from selenium.webdriver import Chrome


class BrowserFactory:

    @staticmethod
    def get_driver():
        driver = Chrome()
        return driver