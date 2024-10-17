from ebay_parser.data_parser import DataParser
from ebay_parser.web_utils import scroll
from ebay_parser.save_utils import write_to_tsv_with_defaults


def main():
    url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?rt=nc&_sop=10"
    parser = DataParser(url)
    items = []

    while len(items) < 2:
        items.extend(parser.passe_page())
        scroll(parser.driver)

    # #cleaned_items = [DataCleaner.clean_data(item) for item in items]
    #
    # print(cleaned_items)
    #
    # DataSaver.save_to_tsv(cleaned_items, "datasets/raw_data/data.tsv")
    # DataSaver.save_to_arff(cleaned_items, "datasets/processed_data/data.arff")

    write_to_tsv_with_defaults(items)


if __name__ == "__main__":
    main()
