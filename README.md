# 📚 Book Scraper – Python Web Scraping from BooksToScrape.com

A simple Python project to **scrape books** from the [Books to Scrape](https://books.toscrape.com) website.  
It collects data such as **title, price, availability, rating, and book cover image**, saving them to a `.csv` file and an `images/` folder.

---

## ✨ Sample Data

| Title                         | Price  | Availability    | Rating | Image               |
|-------------------------------|--------|-----------------|--------|---------------------|
| It's Only the Himalayas        | £45.17 | In stock       | Two    | images-scraper/book_1.jpg   |
| Tipping the Velvet             | £53.74 | In stock       | One    | images-scraper/book_2.jpg   |

---

## 🛠️ Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- [pandas](https://pypi.org/project/pandas/)

---

## 🧪 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/book-scraper.git
cd book-scraper
pip install requests beautifulsoup4 pandas
python scraper.py

```


## 📂 Outputs
ksiazki_z_wielu_stron.csv – books data (CSV)

images-scraper/ – folder with downloaded book covers of simple page
images-many-sites/ – folder with downloaded book covers (many sites)

## 🔄 What does the script scrape?
- Book title
- Price
- Availability
- Rating (as text: One, Two, ..., Five)
- Image – downloaded and saved locally

## ⚙️ Configuration
You can change the number of pages to scrape in scraper.py:
- total_pages = 5  # ← Change this to scrape more pages, e.g. 20 or 50

## 🛡️ Legality
The books.toscrape.com site is created for learning web scraping – scraping its content is allowed and safe.

## 📬 Contact
Questions or want to extend the project with Django/API/GUI?

📧 Email: [karina.zawadzkax@gmail.com]
💬 LinkedIn: [Karina Zawadzka ](https://www.linkedin.com/in/karina-zawadzka-x/)
