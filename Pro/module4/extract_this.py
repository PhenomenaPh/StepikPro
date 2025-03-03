from zipfile import ZipFile


def extract_this(zip_file: str, *args: str):
    with ZipFile(zip_file) as z:

        z.extractall(members=args or None)

    return None
