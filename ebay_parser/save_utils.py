import csv
import os


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
            filtered_row = {key: row.get(key, None) for key in table_fields}
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
    'price',
    'rating',
    'reviews',
    'Screen Size',
    'Storage Capacity',
    'RAM',
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
    'Camera Resolution'
]


def write_to_tsv_with_defaults(data_for_table):
    write_to_tsv(data_for_table, fields)
