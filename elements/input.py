from selenium.webdriver.support import expected_conditions as EC
from elements.base_element import BaseElement


class Input(BaseElement):
    def send_keys(self, keys, clear=True):
        input = self.wait.until(EC.visibility_of_element_located(self.locator))
        if clear:
            input.clear()
        input.send_keys(keys)
