from locators.book_locator import BookLocator
from regex.book_regex import BookRegex


class BookParser:
    STARS = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5
    }

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
        return BookRegex.get_book_price(price_string)

    @property
    def availability(self):
        locator = BookLocator.BOOK_AVAILABILITY
        p_tag = self.parent.select_one(locator)
        return p_tag.text.strip()

    @property
    def stars(self):
        locator = BookLocator.BOOK_STARTS
        p_tag = self.parent.select_one(locator)
        classes = p_tag.attrs.get('class')
        rating = [name for name in classes if name != 'star-rating']
        book_stars = rating[0].lower()
        return BookParser.STARS.get(book_stars)
