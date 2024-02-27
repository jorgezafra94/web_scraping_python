from selenium.webdriver.common.by import By
from locators.quote_locator import QuoteLocator


class QuoteParser:
    """
    Given one of the specific quote divs, find out the data about
    the quote (quote's content, author, tags)
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote{self.content}>'

    @property
    def content(self):
        locator = QuoteLocator.CONTENT
        return self.parent.find_element(By.CSS_SELECTOR, locator)\
            .text\
            .replace('“', '')\
            .replace('”', '')

