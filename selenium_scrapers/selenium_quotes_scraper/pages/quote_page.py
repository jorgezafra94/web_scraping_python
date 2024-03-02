from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from locators.quote_page_locator import QuotePageLocator
from parsers.quote_parser import QuoteParser


class QuotePage:

    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotePageLocator.QUOTE
        quote_html = self.browser.find_elements(By.CSS_SELECTOR, locator)
        return [QuoteParser(q) for q in quote_html]

    @property
    def next_page(self):
        locator = QuotePageLocator.NEXT_PAGE
        try:
            next_page_html = self.browser.find_element(By.CSS_SELECTOR, locator)
            return next_page_html.get_attribute('href')
        except NoSuchElementException:
            return None
