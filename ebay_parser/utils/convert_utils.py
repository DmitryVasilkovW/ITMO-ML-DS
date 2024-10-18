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

        product_condition_values = {
            "восстановленное в хорошем состоянии": ["Отличное состояние - восстановлен",
                                                    "Очень хорошее состояние - восстановлен",
                                                    "Хорошее состояние - восстановлен"],
            "восстановленное в среднем состоянии": ["Среднее состояние - восстановлен"],
            "восстановленное в удовлетворительном состоянии": ["Удовлетворителное состояние - восстановлен"],
            "на запчасти": ["разборка", "на запчасти", "нерабочее",
                            "Для разборки на запчасти или в нерабочем состоянии"],
            "бу": ["БУ", "б/у", "Б/у", "В открытой коробке"],
            "новое": ["новое", "Новый"]
        }

        colour_values = {
            "Black": ["Black", "Черный", "Phantom Black", "Obsidian"],
            "Blue": ["Blue", "Phantom Blue"],
            "Silver": ["Silver", "Aurora Silver"],
            "White": ["White", "Ceramic White"],
            "Grey": ["Grey"],
            "Multicoloured": ["Multicoloured"],
            "Gold": ["Gold"],
            "AT&T": ["AT&T"],
            "Orange": ["Orange"],
            "Red": ["Red"],
            "Yellow": ["Yellow"],
            "Green": ["Green"],
            "Brown": ["Brown"],
            "Purple": ["Deep Purple", "Purple"],
            "Pink": ["Pink"]
        }

        for column in header:
            column_name = column.replace(' ', '_')

            if column_name.lower() == 'product_condition':
                formatted_values = ','.join(f"'{key}'" for key in product_condition_values.keys())
                arff_file.write(f"@ATTRIBUTE {column_name} {{{formatted_values}}}\n")

            elif column_name.lower() == 'colour':
                formatted_values = ','.join(f"'{key}'" for key in colour_values.keys())
                arff_file.write(f"@ATTRIBUTE {column_name} {{{formatted_values}}}\n")

            elif "price" in column or "rating" in column or "reviews" in column or "Size" in column or "Capacity" in column or "RAM" in column or "Camera Resolution MP" in column:
                arff_file.write(f"@ATTRIBUTE {column_name} NUMERIC\n")

            else:
                arff_file.write(f"@ATTRIBUTE {column_name} STRING\n")

        arff_file.write("\n@DATA\n")

        for row in tsv_reader:
            formatted_row = []
            for idx, value in enumerate(row):
                column = header[idx]
                column_name = column.replace(' ', '_')

                if column_name.lower() == 'product_condition':
                    matched_condition = '?'
                    for condition, substrings in product_condition_values.items():
                        if any(substring.lower() in value.lower() for substring in substrings):
                            matched_condition = condition
                            break
                    formatted_row.append(matched_condition)

                elif column_name.lower() == 'colour':
                    matched_colour = '?'
                    for colour, substrings in colour_values.items():
                        if any(substring.lower() in value.lower() for substring in substrings):
                            matched_colour = colour
                            break
                    formatted_row.append(matched_colour)

                else:
                    if value == '':
                        formatted_row.append('?')
                    else:
                        formatted_row.append(value)

            arff_file.write(','.join(formatted_row) + '\n')


def tsv_to_arff_with_defaults(tsv_filename):
    tsv_to_arff(tsv_filename)


tsv_to_arff_with_defaults("../../data/ebay_smartphones_data.tsv")
