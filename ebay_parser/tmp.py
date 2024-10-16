from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from ebay_parser.utils import format_rating

# Настройки для headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Указываем путь к chromedriver
service = ChromeService('/usr/local/bin/chromedriver')

# Запускаем драйвер
driver = webdriver.Chrome(service=service, options=chrome_options)

# Переход на страницу
url = "https://www.ebay.com/itm/256679042909?epid=19063134707&itmmeta=01JABGT73FDZEKY068RH0A6V8H&hash=item3bc3435f5d:g:8X4AAOSwVOJnEBdZ&itmprp=enc%3AAQAJAAAA4IGlUAWZBx1gbu%2FRwYCIK9yGoN%2BoMlxnUoVBjLOGFY7ZQ17atfssaR5GtjMj5vSJrl%2FyOgVE%2FbhSebTMPOMHPFKh%2FNjQY4PkzSDFAsO9DvkXiNwSsOBhbpW21RADidm4AxRckI5Vd0m7dJZOsMyuxHZFhNzYZibCH47Wzc5J%2FW39BjE18bXLdDssWRMhVMbDErkKIM1xVZ6%2BSbfryJQqrjoVTWZOGE04blOrY7iuMHsNl0NCCS8UHAI0EPEEBq%2BxLFBWlAPvN4SUvTGS8CeBUw4mycyoh7niTDhwLyK5pYjg%7Ctkp%3ABk9SR-jx6PDSZA"
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)

# Получение исходного кода страницы
soup = BeautifulSoup(driver.page_source, "html.parser")

rating_div = soup.find("div", class_="ux-summary__star--rating")
if rating_div:
    star_rating = rating_div.find("div", {"role": "img"})
    if star_rating:
        rating_label = star_rating.get("aria-label")
        rating_count, reviews_count = format_rating(rating_label)

        print(f"rating: {rating_count}\n")
        print(f"reviews: {reviews_count}\n")
else:
    print("rating: without_rating" + '\n')
    print("reviews: without_reviews" + '\n')

# Извлечение названий и другой информации
for item in soup.find_all("div", class_="description"):
    title = item.get_text(strip=True)
    print(f"Название: {title}")
    print("-" * 50)

# Закрытие драйвера
driver.quit()
