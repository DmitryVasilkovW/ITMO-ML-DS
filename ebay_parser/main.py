from ebay_parser.parser import parse_ebay
from ebay_parser.data_processing import preprocess_data


def main():
    raw_data = parse_ebay()

    raw_data.to_csv("data/raw_data.tsv", sep='\t', index=False)

    processed_data = preprocess_data(raw_data)
    processed_data.to_csv("data/processed_data.csv", index=False)


if __name__ == "__main__":
    main()
