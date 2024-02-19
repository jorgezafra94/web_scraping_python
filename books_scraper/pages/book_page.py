from bs4 import BeautifulSoup
from locators.book_page_locator import BookPageLocator
from parsers.book_parser import BookParser


class BookPage:

    def __init__(self, raw_page):
        self.soup_page = BeautifulSoup(raw_page, 'html.parser')

    def get_books(self):
        locator = BookPageLocator.BOOK
        list_li_tags = self.soup_page.select(locator)
        list_books = [BookParser(elem) for elem in list_li_tags]
        return list_books

    def get_next_page(self):
        locator = BookPageLocator.NEXT_PAGE
        a_tag = self.soup_page.select_one(locator)
        if a_tag:
            return a_tag.attrs.get('href')
        return None
