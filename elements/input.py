from selenium.webdriver.support import expected_conditions as EC
from elements.base_element import BaseElement


class Input(BaseElement):
    def send_keys(self, keys):
        input = self.wait.until(EC.visibility_of_element_located(self.locator))
        input.send_keys(keys)