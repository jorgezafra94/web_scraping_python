from bs4 import BeautifulSoup
from locators.quote_page_locator import QuotePageLocator
from parsers.quote_parser import QuoteParser


class QuotePage:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotePageLocator.QUOTE
        quote_html = self.soup.select(locator)
        return [QuoteParser(q) for q in quote_html]

    @property
    def next_page(self):
        locator = QuotePageLocator.NEXT_PAGE
        next_page_html = self.soup.select_one(locator)
        if next_page_html:
            return next_page_html.attrs.get('href')
        return None
