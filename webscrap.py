from bs4 import BeautifulSoup
import requests

# Step 1: Fetch the webpage
url = "http://quotes.toscrape.com/"
response = requests.get(url)
response.raise_for_status()

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract specific elements (quotes and authors)
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'"{text}" - {author}')
