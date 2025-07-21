import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs('images-scraper', exist_ok=True)

url = "https://books.toscrape.com/catalogue/page-1.html"
base_url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

data = []

for idx, book in enumerate(books):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()
    availability = book.find('p', class_='instock availability').text.strip()
    rating = book.p['class'][1]

   
    image_relative_url = book.find('img')['src'].replace('../..', '')
    image_url = base_url + image_relative_url.lstrip('/')
    
    image_response = requests.get(image_url)
    image_filename = f'images-scraper/book_{idx+1}.jpg'
    
    with open(image_filename, 'wb') as f:
        f.write(image_response.content)

    data.append({
        'Tytuł': title,
        'Cena': price,
        'Dostępność': availability,
        'Ocena': rating,
        'Obrazek': image_filename
    })


df = pd.DataFrame(data)
df.to_csv('ksiazki_z_obrazkami.csv', index=False, encoding='utf-8-sig')

print("Zapisano dane do ksiazki_z_obrazkami.csv i pobrano zdjęcia.")
