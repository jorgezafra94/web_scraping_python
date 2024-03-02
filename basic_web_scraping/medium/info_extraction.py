import requests
from bs4 import BeautifulSoup


page = requests.get("http://example.com")
html_soup = BeautifulSoup(page.content, 'html.parser')
print(html_soup.prettify())

locator = 'div p a'
link_item = html_soup.select_one(locator)
print(link_item)
print(link_item.attrs['href'])
print(link_item.string)

locator = 'div p'
p_items = html_soup.select(locator)
first_p_content = p_items[0].string
print(first_p_content)



