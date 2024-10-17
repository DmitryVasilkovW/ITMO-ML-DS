import csv
import os
import re


def clean_price(price):
    if price:
        return float(price.replace(' руб.', '').replace(' ', '').replace(',', '.'))
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
    l


def clean_camera_resolution(camera_resolution):
    if camera_resolution:
        return ', '.join(re.findall(r'(\d+\.?\d*)', camera_resolution))
    return None


def write_to_tsv(table_data, table_fields, filename='../data/ebay_smartphones_data.tsv'):
    """
    Создает файл в формате TSV из выбранных полей словаря.

    :param table_data: список словарей с данными
    :param table_fields: список полей, которые нужно записать в TSV
    :param filename: имя выходного файла (по умолчанию '../data/output.tsv')
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        tsv_writer = csv.DictWriter(file, fieldnames=table_fields, delimiter='\t')
        tsv_writer.writeheader()

        for row in table_data:
            filtered_row = {
                'title': clean_title(row.get('title', None)),
                'product condition': row.get('Состояние товара', None),
                'price RUB': clean_price(row.get('price', None)) if row.get('price') else None,
                'rating': row.get('rating', None),
                'reviews': row.get('reviews', None),
                'Screen Size in': clean_screen_size(row.get('Screen Size', None)),
                'Storage Capacity GB': clean_storage_capacity(row.get('Storage Capacity', None)),
                'RAM GB': clean_ram(row.get('RAM', None)),
                'Features': row.get('Features', None),
                'Brand': row.get('Brand', None),
                'Model': row.get('Model', None),
                'Processor': row.get('Processor', None),
                'Chipset Model': row.get('Chipset Model', None),
                'Colour': row.get('Colour', None),
                'Lock Status': row.get('Lock Status', None),
                'Network': row.get('Network', None),
                'Operating System': row.get('Operating System', None),
                'Connectivity': row.get('Connectivity', None),
                'Camera Resolution MP': clean_camera_resolution(row.get('Camera Resolution', None)),
            }
            tsv_writer.writerow(filtered_row)


data = [
    {
        'title': 'НОВОЕ ОБЪЯВЛЕНИЕ Ericsson T65 Solo Cellulare',
        'price': '2 121,59 руб.',
        'rating': None,
        'reviews': None,
        'Состояние товара': 'Б/у',
        'Colore': 'Blu',
        'Capacità di memorizzazione': '1 KB',
        'Marca': 'Ericsson',
        'Modello': 'T65'
    },
    {
        'title': 'НОВОЕ ОБЪЯВЛЕНИЕ Sony Xperia 10 III',
        'price': '8 877,39 руб.',
        'rating': 4.9,
        'reviews': 11,
        'Состояние товара': 'Б/у',
        'EAN': '7311271701125',
        'Processor': 'Octa Core',
        'Screen Size': '6 in',
        'Chipset Model': 'Qualcomm Snapdragon 695 5G',
        'Memory Card Type': 'microSDXC',
        'MPN': 'XQBT52BUKCX',
        'SIM Card Slot': 'Dual SIM (SIM + SIM/Memory Card)',
        'Colour': 'Black',
        'Brand': 'Sony',
        'Network': 'Unlocked',
        'Model': 'Sony Xperia 10 III',
        'Connectivity': 'USB Type-C, 5G, Bluetooth, Wi-Fi, GPS',
        'Style': 'Bar',
        'Operating System': 'Android',
        'Features': 'Water-Resistant, Ultra Wide-Angle Camera, OLED Display, Triple Rear Camera',
        'Storage Capacity': '128 GB',
        'Camera Resolution': '12.0 MP, 8.0 MP',
        'RAM': '6 GB'
    }
]

fields = [
    'title',
    'product condition',
    'price RUB',
    'rating',
    'reviews',
    'Screen Size in',
    'Storage Capacity GB',
    'RAM GB',
    'Features',
    'Brand',
    'Model',
    'Processor',
    'Chipset Model',
    'Colour',
    'Lock Status',
    'Network',
    'Operating System',
    'Connectivity',
    'Camera Resolution MP'
]


def write_to_tsv_with_defaults(data_for_table):
    write_to_tsv(data_for_table, fields)
