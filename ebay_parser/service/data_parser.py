import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


class DataParser:
    def __init__(self, url):
        self.url = url
        self.driver = self.setup_driver()

    def fetch_page(self):
        self.driver.get(self.url)
        time.sleep(5)
        return self.driver.page_source

    def parse_items(self, html):
        soup = BeautifulSoup(html, "html.parser")
        items = []

        rating_div = soup.find("div", class_="star-rating__stars")
        if rating_div:
            rating_label = rating_div.get("aria-label")
            print(f"Рейтинг (из aria-label): {rating_label}")

        for item in soup.find_all("div", class_="description"):
            title = item.get_text(strip=True)
            items.append({"title": title})

            print(f"Название: {title}")
            print("-" * 50)

        return items

    def __setup_driver__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = ChromeService('/usr/local/bin/chromedriver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def close_driver(self):
        self.driver.quit()
