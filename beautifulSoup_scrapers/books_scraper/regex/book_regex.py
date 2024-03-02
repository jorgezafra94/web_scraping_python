import re


class BookRegex:
    BOOK_PRICE_EXPRESSION = '[^0-9](\\d+.\\d+)'
    PAGES_EXPRESSION = '[A-Za-z]+ [0-9]+ of ([0-9]+)'

    @staticmethod
    def get_book_price(raw_price_string):
        expression = BookRegex.BOOK_PRICE_EXPRESSION
        result = re.match(expression, raw_price_string)
        return result.group(1)

    @staticmethod
    def get_pages(raw_pages_text):
        expression = BookRegex.PAGES_EXPRESSION
        result = re.match(expression, raw_pages_text)
        return result.group(1)
