import requests
from bs4 import BeautifulSoup
import pandas as pd


def parse_ebay():
    url = "https://www.ebay.com/b/Electronics/bn_7000259124"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    items = []
    for item in soup.find_all('li', class_="s-item"):
        title = item.find('h3').text
        price = item.find('span', class_="s-item__price").text
        condition = item.find('span', class_="SECONDARY_INFO").text

        items.append({
            "title": title,
            "price": price,
            "condition": condition
        })

    df = pd.DataFrame(items)
    return df
