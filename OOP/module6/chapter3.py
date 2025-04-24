from typing import TextIO


def print_file_content(filename: str):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден")


def non_closed_files(files: TextIO):
    files_open = list()
    for file in files:
        if not file.closed:
            files_open.append(file)

    return files_open


def log_for(logfile: str, date_str: str):
    with (
        open(logfile, "r") as file,
        open(f"log_for_{date_str}.txt", mode="w", encoding="utf-8") as out_file,
    ):
        for line in file:
            line_date_str, line_content = line.split(" ", maxsplit=1)
            if line_date_str == date_str:
                out_file.write(line_content)
