import requests
from pages.quote_page import QuotePage

basic_url = 'https://quotes.toscrape.com/'
url = basic_url

while True:
    page_content = requests.get(url).content
    quote_page = QuotePage(page_content)

    for quote_info in quote_page.quotes:
        print(quote_info)

    if quote_page.next_page:
        print(f"-------------- NEXT PAGE ----------------------------")
        url = basic_url + quote_page.next_page
    else:
        break
