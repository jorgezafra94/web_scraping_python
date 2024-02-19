# web_scraping_python
In this repository our goal is to create web scrappers using python

## Goals
Create two web scrapers to bring information from
* A Quote web site https://quotes.toscrape.com/
* A Book web site https://books.toscrape.com/

## Technologies
* `requests` library to use get http method and bring pages
* `BeautifulSoup` module to be able to navigate in a html page

## Structure
the folders `basic` and `medium` are folders where we practice the basics of beautifulsoup and requests. For example, 
how to get some attributes from a tag, or how to get the text inside a tag, also locators to find the
tag that we need to read in order to get the information that is relevant to us.

`quotes_scraper` and `book_scraper` are the scrapers. Therefore, if you want to run the programs
you just have to run the ``app.py`` file inside the folder.

## Important
We use `pipenv` to install al this packages that is why we have
`Pipfile` and `Pipfile.lock` files to use them as reference for 
requirements needed in order to install all the packages for the program  to run.