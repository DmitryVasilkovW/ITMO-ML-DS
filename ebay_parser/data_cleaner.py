class DataCleaner:
    @staticmethod
    def clean_data(item):
        item['price'] = float(item['price'].replace('$', '').replace(',', ''))
        return item
