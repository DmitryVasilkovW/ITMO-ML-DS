import time
import requests
from bs4 import BeautifulSoup
from .utils import get_headers


class DataParser:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, retries=3):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
        }
        for _ in range(retries):
            try:
                response = requests.get(self.base_url, headers=headers)
                if response.status_code == 200:
                    return response.text
                time.sleep(2)
            except Exception as e:
                print(f"Error fetching page: {e}")
        raise Exception(f"Error fetching page after {retries} retries")

    def parse_items(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = []

        for item in soup.select('.item'):
            title_tag = item.find('h3', class_='title')
            price_tag = item.find('span', class_='price')

            if title_tag and price_tag:
                title = title_tag.text.strip()
                price = price_tag.text.strip()

                items.append({"title": title, "price": price})

        return items
