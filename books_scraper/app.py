"""
This is going to be a book's scraper
https://books.toscrape.com/
"""
import requests
from pages.book_page import BookPage

BASIC_URL = 'https://books.toscrape.com'
PAGE_URL = BASIC_URL + '/catalogue/page-{}.html'


def get_all_books():
    all_books = []
    raw_page = requests.get(BASIC_URL).content
    first_books = BookPage(raw_page)
    all_books.extend(first_books.books)

    for i in range(2, first_books.pages + 1):
        page_url = PAGE_URL.format(i)
        raw_page = requests.get(page_url).content
        new_book_page = BookPage(raw_page)
        all_books.extend(new_book_page.books)

    return all_books
