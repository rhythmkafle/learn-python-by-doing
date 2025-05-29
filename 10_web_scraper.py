import requests
from bs4 import BeautifulSoup as bs

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = bs(response.text, 'html.parser')

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text')
    author = quote.find('span', class_='author')
    tags = [tag.text for tag in quote.find_all('a', class_='tag')]

    print(f"\n{text}\n - {author}\nTags: {', '.join(tags)}")
