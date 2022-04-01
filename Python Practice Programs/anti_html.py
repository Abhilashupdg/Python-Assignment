import requests
import bs4
import logging

logging.basicConfig(filename='anti_html.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


res = requests.get("https://example.com/")

soup = bs4.BeautifulSoup(res.text, "lxml")
logging.info(soup)

page_title = soup.select('p')
logging.info(page_title[0].getText())