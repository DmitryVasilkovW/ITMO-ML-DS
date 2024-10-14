import csv


class DataSaver:
    @staticmethod
    def save_to_tsv(data, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter='\t')
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def save_to_arff(data, file_path):
        with open(file_path, 'w') as file:
            file.write("@RELATION dataset\n")
            for field in data[0].keys():
                file.write(f"@ATTRIBUTE {field} NUMERIC\n")
            file.write("@DATA\n")
            for row in data:
                file.write(','.join(map(str, row.values())) + '\n')
