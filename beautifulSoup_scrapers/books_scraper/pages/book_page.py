from bs4 import BeautifulSoup
from locators.book_page_locator import BookPageLocator
from parsers.book_parser import BookParser
from regex.book_regex import BookRegex


class BookPage:

    def __init__(self, raw_page):
        self.soup_page = BeautifulSoup(raw_page, 'html.parser')

    @property
    def books(self):
        locator = BookPageLocator.BOOK
        list_li_tags = self.soup_page.select(locator)
        list_books = [BookParser(elem) for elem in list_li_tags]
        return list_books

    @property
    def pages(self):
        locator = BookPageLocator.PAGER
        li_tag = self.soup_page.select_one(locator)
        raw_text = li_tag.string.strip()
        return int(BookRegex.get_pages(raw_text))

