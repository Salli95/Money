import requests
from bs4 import BeautifulSoup
import os

def save_text(text, file_path):
  with open(file_path, "w") as file:
      file.write(text)

url = 'https://www.x-rates.com/table/?from=USD&amount=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')
quotes = soup.find_all('table', class_='tablesorter ratesTable')

file_path = "quotes.txt"

for quote in quotes:
  save_text(quote.text,file_path)
  print(quote.text)
