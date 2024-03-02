from selenium import webdriver
from pages.quote_page import QuotePage
import json

url = 'https://quotes.toscrape.com/search.aspx'
chrome_web = webdriver.Chrome()
chrome_web.get(url)
quote_page = QuotePage(chrome_web)

quotes_per_author = quote_page.get_quotes()

with open('quotes.txt', 'w', encoding='utf-8') as file:
    json.dump(quotes_per_author, file, sort_keys=True, indent=4, ensure_ascii=False)
