from ebay_parser.data_parser import DataParser
from ebay_parser.utils.web_utils import scroll
from ebay_parser.utils.save_utils import write_to_tsv_with_defaults


def main():
    url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?rt=nc&_sop=10"
    parser = DataParser(url)
    items = []

    while len(items) < 400:
        items.extend(parser.passe_page())
        scroll(parser.driver)

    write_to_tsv_with_defaults(items)


if __name__ == "__main__":
    main()
