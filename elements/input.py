from selenium.webdriver.support import expected_conditions as EC
from elements.base_element import BaseElement


class Input(BaseElement):
    def send_keys(self, keys, clear=True):
        input_field = self.wait.until(EC.visibility_of_element_located(self.locator))
        if clear:
            self.clear_input(input_field)
        input_field.send_keys(keys)

    def clear_input(self, input_field):
        input_field.clear()