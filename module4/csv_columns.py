import csv


def csv_columns(file_path: str) -> dict:

    with open(file_path, encoding="utf-8") as file:
        rows = list(csv.reader(file))
        columns_dict = {column: values for column, *values in list(zip(*rows))}

    return columns_dict
