from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from elements.element import Element
from .base_page import BasePage
from elements.label import Label


class ScrollPage(BasePage):
    UNIQUE_ELEMENT = (By.XPATH, '//div[contains(@class, "example")]')
    PARAGRAPH = "(//div[contains(@class, 'jscroll-added')])[{}]"
    SCROLL = (By.CSS_SELECTOR, "div.scroll")

    def __init__(self, driver):
        super().__init__(driver)
        self.unique_element = Label(driver, self.UNIQUE_ELEMENT)
        self.scroll_element = Element(driver, self.SCROLL, description="")

    def get_all_paragraphs(self):
        self.logger.info("Получение всех параграфов на странице")

        inner_html = self.scroll_element.get_attribute("innerHTML")

        soup = BeautifulSoup(inner_html, 'html.parser')
        paragraphs = soup.find_all('div', class_='jscroll-added')
        self.logger.info(f"Найдено {len(paragraphs)} параграфов")
        
        return paragraphs

    def scroll_to_paragraph_count(self, target_count):
        self.logger.info(f"Начало прокрутки до {target_count} параграфов")
        while True:
            current_count = len(self.get_all_paragraphs())
            self.logger.info(f"Текущее количество параграфов: {current_count}")

            if current_count >= target_count:
                self.logger.info("Достигнуто необходимое количество параграфов")
                break

            locator = (By.XPATH, self.PARAGRAPH.format(current_count))
            last_paragraph = Label(self.driver, locator, description="Infinite Scroll Page -> Paragraph")
            last_paragraph.scroll_into_view()

        return current_count