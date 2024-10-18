import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from ebay_parser.utils.data_utils import format_label
from ebay_parser.utils.data_utils import format_rating
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataParser:
    def __init__(self, url):
        self.url = url
        self.driver = self.__setup_driver()
        self.soup = BeautifulSoup(self.fetch_page(), 'html.parser')
        self.counter = 0

    def fetch_page(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.s-item'))
        )
        return self.driver.page_source

    @staticmethod
    def fetch_page_with_url(url, driver):
        driver.get(url)
        time.sleep(5)
        return driver.page_source

    def passe_page(self):
        try:
            items = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.s-item'))
            )
        except Exception as e:
            print(f"Error while retrieving items: {e}")
            return []

        i = 0
        item_list = []
        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, '.s-item__title').text
                price = item.find_element(By.CSS_SELECTOR, '.s-item__price').text
                link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                item_info = {'title': title, 'price': price}
                item_list.append(self.parse_item_params(link, item_info))
            except Exception as e:
                print(f"Error while retrieving information about an item: {e}")
                i += 1
                if i > 3:
                    break
                continue

        return item_list

    def parse_item_params(self, url, item_info):
        driver = self.__setup_driver()
        page_content = self.fetch_page_with_url(url, driver)

        if not page_content:
            print("Error: failed to load the page.")
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

        self.counter += 1
        print(str(self.counter) + "\n")
        return item_info

    def close_driver(self):
        self.driver.quit()

    @staticmethod
    def __setup_driver():
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = ChromeService('/usr/local/bin/chromedriver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
