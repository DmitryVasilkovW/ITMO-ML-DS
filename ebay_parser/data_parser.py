import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from utils import format_label
from utils import format_rating
from selenium.webdriver.common.by import By


class DataParser:
    def __init__(self, url):
        self.url = url
        self.driver = self.__setup_driver()
        self.soup = BeautifulSoup(self.fetch_page(), 'html.parser')
        self.c = 0

    def fetch_page(self):
        self.driver.get(self.url)
        time.sleep(5)
        return self.driver.page_source

    def fetch_page_with_url(self, url):
        self.driver.get(url)
        time.sleep(5)
        return self.driver.page_source

    def passe_page(self):
        items = self.driver.find_elements(By.CSS_SELECTOR, '.s-item')
        data = []
        for item in items:
            title = item.find_element(By.CSS_SELECTOR, '.s-item__title').text
            price = item.find_element(By.CSS_SELECTOR, '.s-item__price').text
            link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            data.append({'title': title, 'price': price, 'link': link})
        return data

    def parse_item(self):
        items = self.soup.find_all('li', class_='s-item')

        item_list = []
        i = 0

        for item in items:
            if i > 1:
                break
            i += 1

            link_tag = item.find('a', class_='s-item__link')
            price_tag = item.find('span', class_='s-item__price')
            item_info = "prise: " + price_tag.text.strip().replace('\xa0', '').replace(' руб.', '').replace(' ',
                                                                                                            '').replace(
                ',', '.') + "\n"

            item_list.append(self.parse_items(link_tag.get('href'), item_info))

        return item_list

    def parse_items(self, url, item_info):
        items = []
        page_content = self.fetch_page_with_url(url)

        if not page_content:
            print("Ошибка: не удалось загрузить страницу.")
            return items

        soup = BeautifulSoup(page_content, 'html.parser')

        rating_div = soup.find("div", class_="ux-summary__star--rating")
        if rating_div:
            star_rating = rating_div.find("div", {"role": "img"})
            if star_rating:
                rating_label = star_rating.get("aria-label")
                rating_count, reviews_count = format_rating(rating_label)

                item_info += f"rating: {rating_count}\n"
                item_info += f"reviews: {reviews_count}\n"
        else:
            item_info += "rating: without_rating" + '\n'
            item_info += "reviews: without_reviews" + '\n'

        features = soup.find_all('dl', {'data-testid': 'ux-labels-values'})

        characteristics = {}
        for feature in features:
            label = feature.find('dt').get_text(strip=True)
            value = feature.find('dd').get_text(strip=True)
            characteristics[label] = value

        for label, value in characteristics.items():
            item_info += f"{format_label(label)}: {value}"
            item_info += "\n"

        items.append(item_info)

        self.c += 1
        print(str(self.c) + "\n")
        return items

    def close_driver(self):
        self.driver.quit()

    @staticmethod
    def __setup_driver():
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = ChromeService('/usr/local/bin/chromedriver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
