import requests
from bs4 import BeautifulSoup

url = 'https://www.x-rates.com/table/?from=USD&amount=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')
quotes = soup.find_all('table', class_='tablesorter ratesTable')
for quote in quotes:
  print(quote.text)
