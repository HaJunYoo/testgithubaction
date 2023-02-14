import datetime
import requests
from bs4 import BeautifulSoup


print(f"hello! It's {datetime.datetime.now()}. Start Crawling")

url = 'https://ridibooks.com/category/new-releases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.title_text')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
