import pytest
from browser.browser import Browser


@pytest.fixture(scope='function')
def browser():
    browser = Browser()
    yield browser
    browser.quit()