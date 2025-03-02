import keyword
import re


def normalize_jpeg(filename: str) -> str:
    mod_string = re.sub("(jpeg|jpg)$", "jpg", filename, flags=re.I)

    return mod_string


def normalize_whitespace(string: str) -> str:
    mod_string = re.sub("\s+", " ", string)
    return mod_string


def replace_keywords(string: str) -> str:
    kw_list = rf"\b{r'\b|\b'.join(keyword.kwlist)}\b"

    mod_string = re.sub(rf"{kw_list}", "<kw>", string, flags=re.I)
    print(kw_list)

    print(mod_string)


def replace_first_two_digits(string: str) -> str:
    mod_text = re.sub(r"\b(\w)(\w)(\w*)", r"\2\1\3", string)

    return mod_text


def replace_brackets(string: str) -> str:
    regex_pattern = r"(\d+)\((\w*)\)"

    while "(" in string:
        string = re.sub(regex_pattern, lambda x: int(x[1]) * x[2], string, count=1)

    return string


def repeat_words(string: str) -> str:
    regex_pattern = r"(\b\w+\b)(\W+\1\b)"

    string = re.sub(regex_pattern, lambda x: x[1], string)

    return string


if __name__ == "__main__":
    example_var = "beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik"
    print(repeat_words(example_var))
