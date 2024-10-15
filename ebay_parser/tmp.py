from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

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
url = "https://www.ebay.com/p/12063729299?iid=235783543822&rt=nc#UserReviews"
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)

# Получение исходного кода страницы
soup = BeautifulSoup(driver.page_source, "html.service")

rating_div = soup.find("div", class_="star-rating__stars")
if rating_div:
    rating_label = rating_div.get("aria-label")
    print(f"Рейтинг (из aria-label): {rating_label}")

# Извлечение названий и рейтингов товаров
for item in soup.find_all("div", class_="description"):
    title = item.get_text(strip=True)

    # Поиск рейтинга через div с классом star-rating__stars

    print(f"Название: {title}")
    print("-" * 50)

# Закрытие драйвера
driver.quit()
