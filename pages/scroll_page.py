from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from .base_page import BasePage
from elements.label import Label


class ScrollPage(BasePage):
    PARAGRAPH = "(//div[contains(@class, 'jscroll-added')])[{}]"

    def get_all_paragraphs(self):
        self.logger.info("Получение всех параграфов на странице")
        page_source = self.driver.get_page_source()
        soup = BeautifulSoup(page_source, 'html.parser')
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
