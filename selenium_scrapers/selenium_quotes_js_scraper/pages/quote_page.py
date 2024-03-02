from locators.page_locator import PageLocator
from parsers.quote_parser import QuoteParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.regex_utils import RegexUtils


class QuotePage:

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def __getting_options_from_select_item(select_item):
        options = select_item.options
        cleaned_options = list(filter(RegexUtils.getting_valid_options, options))
        text_options = list(map(lambda elem: elem.text.strip(), cleaned_options))
        return text_options

    def __get_select_item(self, locator):
        dropdown_item = self.browser.find_element(By.CSS_SELECTOR, locator)
        select_item = Select(dropdown_item)
        return select_item

    def __get_drop_down_info(self, locator):
        select_item = self.__get_select_item(locator)
        dropdown_options = self.__getting_options_from_select_item(select_item)
        return dropdown_options

    def get_author_info(self):
        locator = PageLocator.AUTHOR_DROPDOWN
        author_options = self.__get_drop_down_info(locator)
        return author_options

    def get_tag_info(self):
        locator = PageLocator.TAG_DROPDOWN
        tag_options = self.__get_drop_down_info(locator)
        return tag_options

    def get_search_btn(self):
        locator = PageLocator.SEARCH_BTN
        button_item = self.browser.find_element(By.CSS_SELECTOR, locator)
        return button_item

    def get_quotes_from_tag_selected(self, button_item):
        button_item.click()
        locator = PageLocator.RESULTS
        results = self.browser.find_elements(By.CSS_SELECTOR, locator)
        quotes = [QuoteParser(result) for result in results]
        return [quote.content for quote in quotes]

    def get_quotes_from_author_selected(self):
        tag_quotes = dict()
        tag_options = self.get_tag_info()
        for tag in tag_options:
            tag_dropdown = self.__get_select_item(PageLocator.TAG_DROPDOWN)
            tag_dropdown.select_by_visible_text(tag)
            search_btn = self.get_search_btn()
            list_quotes = self.get_quotes_from_tag_selected(search_btn)
            tag_quotes[tag] = list_quotes
        return tag_quotes

    def get_quotes(self):
        quote_author = dict()
        author_options = self.get_author_info()
        for author in author_options:
            author_dropdown = self.__get_select_item(PageLocator.AUTHOR_DROPDOWN)
            author_dropdown.select_by_visible_text(author)
            tag_quotes = self.get_quotes_from_author_selected()
            quote_author[author] = tag_quotes
        return quote_author
