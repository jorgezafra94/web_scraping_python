import re
from locators.book_locator import BookLocator


def clean_price(price):
    expression = '[^0-9](\\d+.\\d+)'
    result = re.match(expression, price)
    return result.group(1)


def star_word_to_num(word):
    match word.lower():
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5


class BookParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book Title: {self.title}, Price: {self.price}, Stars: {self.stars}, Available: {self.availability}>'

    @property
    def title(self):
        locator = BookLocator.BOOK_TITLE
        a_tag = self.parent.select_one(locator)
        book_title = a_tag.attrs.get('title')
        return book_title

    @property
    def price(self):
        locator = BookLocator.BOOK_PRICE
        p_tag = self.parent.select_one(locator)
        price_string = p_tag.string
        real_price = float(clean_price(price_string))
        return real_price

    @property
    def availability(self):
        locator = BookLocator.BOOK_AVAILABILITY
        p_tag = self.parent.select_one(locator)
        return p_tag.text.strip()

    @property
    def stars(self):
        locator = BookLocator.BOOK_STARTS
        p_tag = self.parent.select_one(locator)
        book_stars = p_tag.attrs.get('class')[1]
        return star_word_to_num(book_stars)
