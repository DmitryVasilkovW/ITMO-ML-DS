import csv
import os


def tsv_to_arff(tsv_filename, arff_filename='../../data/ebay_smartphones_data.arff', relation_name="smartphone_data"):
    os.makedirs(os.path.dirname(arff_filename), exist_ok=True)

    with open(tsv_filename, mode='r', newline='', encoding='utf-8') as tsv_file, open(arff_filename, mode='w',
                                                                                      newline='',
                                                                                      encoding='utf-8') as arff_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        header = next(tsv_reader)

        arff_file.write(f"@RELATION {relation_name}\n\n")

        for column in header:
            if "price" in column or "rating" in column or "reviews" in column or "Size" in column or "Capacity" in column or "RAM" in column or "Camera Resolution MP" in column:
                arff_file.write(f"@ATTRIBUTE {column.replace(' ', '_')} NUMERIC\n")
            else:
                arff_file.write(f"@ATTRIBUTE {column.replace(' ', '_')} STRING\n")

        arff_file.write("\n@DATA\n")

        for row in tsv_reader:
            formatted_row = []
            for value in row:
                if value == '':
                    formatted_row.append('?')
                else:
                    formatted_row.append(value)

            arff_file.write(','.join(formatted_row) + '\n')


def tsv_to_arff_with_defaults(tsv_filename):
    tsv_to_arff(tsv_filename)


def arff_to_csv(arff_filename, csv_filename='../data/ebay_smartphones_data.csv'):
    os.makedirs(os.path.dirname(csv_filename), exist_ok=True)

    with open(arff_filename, mode='r', encoding='utf-8') as arff_file, open(csv_filename, mode='w', newline='',
                                                                            encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        data_section = False
        for line in arff_file:
            line = line.strip()

            if line.lower() == '@data':
                data_section = True
                continue

            if data_section and not line.startswith('%'):
                csv_writer.writerow(line.split(','))


def arff_to_csv_with_defaults(arff_filename):
    arff_to_csv(arff_filename)


tsv_to_arff_with_defaults("../../data/ebay_smartphones_data.tsv")
