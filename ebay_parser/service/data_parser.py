import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


class DataParser:
    def __init__(self, url):
        self.url = url
        self.driver = self.__setup_driver()
        self.soup = BeautifulSoup(self.fetch_page(), 'html.parser')

    def fetch_page(self):
        self.driver.get(self.url)
        time.sleep(5)
        return self.driver.page_source

    def fetch_page_with_url(self, url):
        self.driver.get(url)
        time.sleep(5)
        return self.driver.page_source

    def parse_page(self):
        items = self.soup.find_all('li', class_='s-item')

        item_list = []
        i = 0

        for item in items:
            if i > 4:
                break

            link_tag = item.find('a', class_='s-item__link')

            item_list.append(self.parse_items(link_tag.get('href')))
            i += 1

        return item_list

    def parse_items(self, url):
        items = []
        page_content = self.fetch_page_with_url(url)

        # Проверка на пустой контент
        if not page_content:
            print("Ошибка: не удалось загрузить страницу.")
            return items

        soup = BeautifulSoup(page_content, 'html.parser')

        # Поиск рейтинга
        rating_div = soup.find("div", class_="star-rating__stars")
        if rating_div:
            rating_label = rating_div.get("aria-label")
            if rating_label:
                print(f"Рейтинг (из aria-label): {rating_label}")
            else:
                print("aria-label не найдено в div рейтинга.")
        else:
            print("Рейтинг не найден.")

        # Поиск описаний товаров
        # descriptions = soup.find_all("div", class_="ux-labels-values ux-labels-values--inline col-6 ux-labels-values--condition")
        # if not descriptions:
        #     print("Товары не найдены.")
        #     return items
        #
        # for item in descriptions:
        #     # Ищем <dd> элемент, который содержит описание
        #     description = item.find("dd")
        #
        #     if description:
        #         title = description.get_text(strip=True)
        #         items.append({"title": title})
        #         print(f"Описание: {title}")
        #         print("-" * 50)
        #     else:
        #         print("Описание отсутствует.")

        features = soup.find_all('dl', {'data-testid': 'ux-labels-values'})

        # Извлекаем название и значение каждой характеристики
        characteristics = {}
        for feature in features:
            label = feature.find('dt').get_text(strip=True)
            value = feature.find('dd').get_text(strip=True)
            characteristics[label] = value

        # Выводим результаты
        for label, value in characteristics.items():
            print(f"{label}: {value}")

        return items

    def parse_old_items(self, url):
        items = []
        soup = BeautifulSoup(self.fetch_page_with_url(url), 'html.parser')

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

    def close_driver(self):
        self.driver.quit()

    def __setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = ChromeService('/usr/local/bin/chromedriver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
