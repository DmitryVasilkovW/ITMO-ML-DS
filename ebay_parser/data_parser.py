import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from data_utils import format_label
from data_utils import format_rating
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
        item_list = []
        i = 0
        for item in items:
            if i > 4:
                break
            i += 1

            title = item.find_element(By.CSS_SELECTOR, '.s-item__title').text
            price = item.find_element(By.CSS_SELECTOR, '.s-item__price').text
            link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            item_info = {'title': title, 'price': price}
            item_list.append(self.parse_item_params(link, item_info))

        return item_list

    def parse_item_params(self, url, item_info):
        page_content = self.fetch_page_with_url(url)

        if not page_content:
            print("Ошибка: не удалось загрузить страницу.")
            return item_info

        soup = BeautifulSoup(page_content, 'html.parser')

        rating_div = soup.find("div", class_="ux-summary__star--rating")
        if rating_div:
            star_rating = rating_div.find("div", {"role": "img"})
            if star_rating:
                rating_label = star_rating.get("aria-label")
                rating_count, reviews_count = format_rating(rating_label)

                item_info.update({'rating': rating_count})
                item_info.update({'reviews': reviews_count})
        else:
            item_info.update({'rating': None})
            item_info.update({'reviews': None})

        features = soup.find_all('dl', {'data-testid': 'ux-labels-values'})

        characteristics = {}
        for feature in features:
            label = feature.find('dt').get_text(strip=True)
            value = feature.find('dd').get_text(strip=True)
            characteristics[label] = value

        for label, value in characteristics.items():
            item_info.update({str(format_label(label)): value})

        self.c += 1
        print(str(self.c) + "\n")
        return item_info

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
