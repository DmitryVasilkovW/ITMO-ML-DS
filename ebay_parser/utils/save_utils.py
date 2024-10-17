import csv
import os

from ebay_parser.utils.clean_utils import clean_title, clean_price, clean_screen_size, clean_storage_capacity, clean_ram, \
    clean_camera_resolution


def write_to_tsv(table_data, table_fields, filename='../data/ebay_smartphones_data.tsv'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        tsv_writer = csv.DictWriter(file, fieldnames=table_fields, delimiter='\t')

        if file.tell() == 0:
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
