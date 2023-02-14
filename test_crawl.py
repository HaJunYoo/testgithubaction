import datetime
import requests
from bs4 import BeautifulSoup

print(f"Hello! It's {datetime.datetime.now()}. Start crawling")

url = 'https://ridibooks.com/category/bestsellers/2200?page=1'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
# book_services = soup.select('.fig-9so5j3')
books_name = soup.select('.fig-z0an5g')
books_ranks = soup.select('.fig-hm7n2o')
books_context = soup.select('.fig-1uif0qw')


books = []
for n, r, c in zip(books_name, books_ranks, books_context) :
    name = n.text.strip()
    ranking = r.text.strip()
    context = c.text.strip()
    temp_data = {
        'ranking': ranking,
        'name': name,
        'context': context
    }

    if name:
        books.append(temp_data)
    else:
        continue

for book in books:
    print(book)
    print()