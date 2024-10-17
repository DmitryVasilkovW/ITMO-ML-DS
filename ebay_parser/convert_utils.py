import csv


def tsv_to_arff(tsv_filename, arff_filename, relation_name="smartphone_data"):
    with open(tsv_filename, mode='r', newline='', encoding='utf-8') as tsv_file, open(arff_filename, mode='w',
                                                                                      newline='',
                                                                                      encoding='utf-8') as arff_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        header = next(tsv_reader)

        arff_file.write(f"@RELATION {relation_name}\n\n")

        for column in header:
            if "price" in column or "rating" in column or "reviews" in column or "Size" in column or "Capacity" in column or "RAM" in column:
                arff_file.write(f"@ATTRIBUTE {column.replace(' ', '_')} NUMERIC\n")
            else:
                arff_file.write(f"@ATTRIBUTE {column.replace(' ', '_')} STRING\n")

        arff_file.write("\n@DATA\n")

        # Запись данных
        for row in tsv_reader:
            formatted_row = []
            for value in row:
                # Если ячейка пустая, используем '?', как принято в ARFF
                if value == '':
                    formatted_row.append('?')
                else:
                    formatted_row.append(value)

            arff_file.write(','.join(formatted_row) + '\n')
