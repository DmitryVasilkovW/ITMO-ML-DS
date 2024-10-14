from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = ChromeService('/usr/local/bin/chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.ebay.com/p/12063729299?iid=235783543822&rt=nc#UserReviews"
driver.get(url)

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

for item in soup.find_all("div", class_="description"):
    title = item.get_text(strip=True)
    rating_div = item.find("div", class_="star-rating")
    if rating_div:
        rating = rating_div['data-stars']

    print(f"Название: {title}")
    if rating_div:
        print(f"Рейтинг: {rating}")
    print("-" * 50)

driver.quit()
