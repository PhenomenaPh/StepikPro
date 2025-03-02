from typing import Generator


def is_phone_number(phone: str) -> bool:
    groups = phone.split("-")
    groups_val = list(map(len, groups)) + [groups[0]]
    if groups_val in ([1, 3, 3, 2, 2, '7'], [1, 3, 4, 4, '8']):
        chars = "".join(groups)
        return all(i.isdigit() for i in chars)


def get_all_numbers(text: str) -> Generator[str, None, None]:
    for c in range(len(text)):
        text_chuck = text[c: c + 15]

        if is_phone_number(text_chuck):
            yield text_chuck


if __name__ == "__main__":
    text = input()

    for text in get_all_numbers(text):
        print(text)
