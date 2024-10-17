from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Настройка драйвера
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = ChromeService('/usr/local/bin/chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем страницу eBay
driver.get('https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?LH_BIN=1&rt=nc&_sop=10')


# Собираем данные с первой страницы
def collect_data():
    items = driver.find_elements(By.CSS_SELECTOR, '.s-item')
    data = []
    for item in items:
        title = item.find_element(By.CSS_SELECTOR, '.s-item__title').text
        price = item.find_element(By.CSS_SELECTOR, '.s-item__price').text
        link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        data.append({'title': title, 'price': price, 'link': link})
    return data


# Прокрутка и сбор данных с нескольких страниц
all_data = []
while len(all_data) < 1000:
    print(len(all_data))
    all_data.extend(collect_data())

    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'a.pagination__next')
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()
        time.sleep(5)  # Ожидание загрузки следующей страницы
    except Exception as e:
        print("Не удалось найти кнопку перехода:", e)
        break

# Закрытие драйвера
driver.quit()

# Вывод данных
for item in all_data:
    print(item)
