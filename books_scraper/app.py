"""
This is going to be a book's scraper
https://books.toscrape.com/
"""
import requests
from pages.book_page import BookPage

basic_url = 'https://books.toscrape.com/'
url = basic_url

while True:
    raw_page = requests.get(url).content
    book_page = BookPage(raw_page)
    for book in book_page.get_books():
        print(book)

    next_page_url = book_page.get_next_page()
    if next_page_url:
        print(f"-------------- NEXT PAGE ----------------------------")
        if 'catalogue' not in next_page_url:
            next_page_url = 'catalogue/' + next_page_url
        url = basic_url + next_page_url
    else:
        break
