from ebay_parser.data_cleaner import DataCleaner
from ebay_parser.service.data_parser import DataParser
from ebay_parser.data_saver import DataSaver


def main():
    # url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
    url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?rt=nc&_sop=10"
    parser = DataParser(url)

    html = parser.fetch_page()

    items = parser.parse_page()

    # #cleaned_items = [DataCleaner.clean_data(item) for item in items]
    #
    # print(cleaned_items)
    #
    # DataSaver.save_to_tsv(cleaned_items, "datasets/raw_data/data.tsv")
    # DataSaver.save_to_arff(cleaned_items, "datasets/processed_data/data.arff")

    print(items)


if __name__ == "__main__":
    main()
