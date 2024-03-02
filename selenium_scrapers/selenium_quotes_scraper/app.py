from selenium import webdriver
from pages.quote_page import QuotePage

url = 'https://quotes.toscrape.com/'
chrome_web = webdriver.Chrome()

while True:
    chrome_web.get(url)
    quote_page = QuotePage(chrome_web)

    for quote_info in quote_page.quotes:
        print(quote_info)

    if quote_page.next_page:
        print(f"-------------- NEXT PAGE ----------------------------")
        url = quote_page.next_page
    else:
        break
