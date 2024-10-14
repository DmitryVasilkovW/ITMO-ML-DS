from ebay_parser.data_cleaner import DataCleaner
from ebay_parser.data_parser import DataParser
from ebay_parser.data_saver import DataSaver


def main():
    url = "https://www.ebay.com/b/Electronics/bn_7000259124"
    parser = DataParser(url)

    # Вызов метода fetch_page() без аргументов, так как URL передан в конструктор
    html = parser.fetch_page()

    # Парсинг товаров
    items = parser.parse_items(html)

    # Очистка данных
    cleaned_items = [DataCleaner.clean_data(item) for item in items]

    print(cleaned_items)

    # Сохранение данных
    DataSaver.save_to_tsv(cleaned_items, "datasets/raw_data/data.tsv")
    DataSaver.save_to_arff(cleaned_items, "datasets/processed_data/data.arff")


if __name__ == "__main__":
    main()
