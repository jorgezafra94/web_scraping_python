from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>
'''

processed_html = BeautifulSoup(SIMPLE_HTML, 'html.parser')

ul_item = processed_html.ul
li_items = ul_item.find_all('li')
print(li_items)

p_item = processed_html.find_all('p', attrs={'class': 'subtitle'})
print(p_item)

