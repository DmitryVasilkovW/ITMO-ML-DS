import re


def clean_price(price):
    if price:
        match = re.search(r'(\d+[\.,]?\d*)', price.replace(' ', ''))
        if match:
            return float(match.group(1).replace(',', '.'))
    return None


def clean_title(title):
    if title:
        return title.replace('НОВОЕ ОБЪЯВЛЕНИЕ', '')
    return None


def clean_screen_size(screen_size):
    if screen_size:
        match = re.search(r'(\d+)', screen_size)
        if match:
            return match.group(1)
    return None


def clean_storage_capacity(storage_capacity):
    if storage_capacity:
        match = re.search(r'(\d+)', storage_capacity)
        if match:
            return match.group(1)
    return None


def clean_ram(ram):
    if ram:
        match = re.search(r'(\d+)', ram)
        if match:
            return match.group(1)
    return None


def clean_camera_resolution(camera_resolution):
    if camera_resolution:
        return ', '.join(re.findall(r'(\d+\.?\d*)', camera_resolution))
    return None
