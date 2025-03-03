def find_size(value: int, value_type: str, lowest=True) -> int:
    values_dict = {"MB": 2, "KB": 1, "GB": 3, "B": 0}
    new_value = None
    if lowest:
        new_value = value * 1024 ** values_dict[value_type]
    else:
        del_count = 0
        while value % 1024 != value:
            value /= 1024
            del_count += 1
        value_type = list(
            key for key, value in values_dict.items() if value == del_count
        )[0]
        new_value = str(round(value))

    return new_value, value_type


def get_file_info(filename: str) -> dict:
    """
    Extracts file information from a given file.

    :param filename: The name of the file to be processed.
    :return: A dictionary containing the file information.

    The method reads the file, extracts the file type, file name, size and size_type for each line,
    and updates a dictionary with the following structure:
    {
        <file_type>: {
            "files": [<list_of_files>],
            "size": <total_size_of_files>,
            "size_type": "B"
        }
    }
    """
    files_dict = {}

    with open(filename, "r", encoding="utf-8") as tf:
        files = tf.read().splitlines()

        for file in files:
            temp_file = file.split()

            file_type = temp_file[0][temp_file[0].index(".") :]
            file_name = temp_file[0]
            size_type = temp_file[2]
            size = find_size(int(temp_file[1]), size_type)[0]

            if file_type not in files_dict:
                files_dict[file_type] = {
                    "files": [file_name],
                    "size": size,
                    "size_type": "B",
                }

            else:
                files_dict[file_type]["files"].append(file_name)
                files_dict[file_type]["size"] += size

    return files_dict


def output_file_info(file_info: dict):

    for file, info in sorted(file_info.items()):
        print("\n".join(sorted(info["files"])))
        print("-" * 10)
        print(
            f"Summary: {' '.join(find_size(info['size'], value_type='B', lowest=False))}"
        )
        print()
    return None


def main():
    files_dict = get_file_info("files.txt")
    output_file_info(files_dict)


if __name__ == "__main__":
    main()
