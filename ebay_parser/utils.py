def clean_price(price):
    return float(price.replace('$', '').replace(',', ''))
