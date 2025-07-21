import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time


os.makedirs('images-many-sites', exist_ok=True)

base_url = "https://books.toscrape.com/"
start_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []
book_counter = 1  # Do nadawania nazw zdjęciom

# sites
total_pages = 5

for page_num in range(1, total_pages + 1):
    url = start_url.format(page_num)
    print(f"Scrapuję stronę: {url}")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Nie udało się załadować strony {url}")
        continue

    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.p['class'][1]

        image_relative_url = book.find('img')['src'].replace('../..', '')
        image_url = base_url + image_relative_url.lstrip('/')
        image_filename = f'images-many-sites/book_{book_counter}.jpg'

        # Pobierz obrazek
        img_response = requests.get(image_url)
        with open(image_filename, 'wb') as f:
            f.write(img_response.content)

        # Zcollecting data
        data.append({
            'Tytuł': title,
            'Cena': price,
            'Dostępność': availability,
            'Ocena': rating,
            'Obrazek': image_filename
        })

        book_counter += 1

    # delay
    time.sleep(1)

df = pd.DataFrame(data)
df.to_csv('ksiazki_z_wielu_stron.csv', index=False, encoding='utf-8-sig')

print(f"\n✅ Gotowe! Zebrano {len(data)} książek ze stron 1–{total_pages}.")
print("📁 Dane zapisane do: ksiazki_z_wielu_stron.csv")
print("🖼️ Obrazki zapisane w folderze: images/")
