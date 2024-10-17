def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'
    }


def format_price(price_str):
    return float(price_str.replace('$', '').replace(',', ''))


def format_label(label):
    return label.replace("Marke", "Brand")


def format_rating(rating):
    if len(rating) == 0:
        return 0.0, 0

    parts = rating.split(',')

    rating_str = parts[0].split()[0]
    rating_count = float(rating_str)

    reviews_count_str = parts[1].split()[2]
    reviews_count = int(reviews_count_str)

    return rating_count, reviews_count
