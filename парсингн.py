import requests
from bs4 import BeautifulSoup

url = 'https://www.x-rates.com/table/?from=USD&amount=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='tablesorter ratesTable')

VAR=[
    "Russian Ruble",
    "Euro",
    "Kazakhstani Tenge"
    ]
Valut={
    "USD":1
} 

if table :
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1:
            currency = cells[0].text.strip()
            rate = cells[1].text.strip()
            if currency in VAR:
             Valut[currency]=rate
            #  print(f"{currency}: {rate}")
            
else:
    print("Таблица не найдена на странице.")
# print(Valut)

for key, value in Valut.items():
  print("{0}: {1}".format(key,value))