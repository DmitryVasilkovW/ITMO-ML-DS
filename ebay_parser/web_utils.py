from selenium.webdriver.common.by import By
import time


def scroll(driver):
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'a.pagination__next')
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()
        time.sleep(5)
    except Exception as e:
        print("Не удалось найти кнопку перехода:", e)
