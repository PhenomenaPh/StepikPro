import re
from re import search


def find_phone_number(number: str) -> str:
    num_regex = (
        r"(?P<area>\d{1,3})"  # Area code: 1-3 digits
        r"(?P<sep>[- ])"  # Separator: hyphen or space
        r"(?P<prefix>\d{1,3})"  # Prefix: 1-3 digits
        r"(?P=sep)"  # Backreference to separator
        r"(?P<number>\d{4,10})"  # Line number: 4-10 digits
    )
    search_res = search(pattern=num_regex, string=number).groupdict()
    result_str = f"Код страны: {search_res['area']}, Код города: {search_res['prefix']}, Номер: {search_res['number']}"

    return result_str


def find_begeek_login(login: str) -> bool:
    login_regex = (
        r"^_"  # First symbol is _
        r"\d{1,}"  # Then we have number of digits from 1 to many
        r"[a-zA-Z]*"  # Then we have any number of letters from a to z or A to Z
        r"_?$"  # Ending with optional underscore
    )
    return bool(search(pattern=login_regex, string=login))


def find_syllables(text: str) -> str | None:
    # Looking for repeating syllables (2 or more same syllables)
    regex = r"\b(\w+?)\1\b"

    regex_search = search(regex, text)

    if regex_search:
        return regex_search.group()


def find_begeek() -> None:
    input_lines = map(str.strip, open(0))
    bee, geek = 0, 0

    bee_regex = r"bee.*bee"
    geek_regex = r"\bgeek\b"

    for line in input_lines:
        if search(bee_regex, line):
            bee += 1
        if search(geek_regex, line):
            geek += 1

    print(bee, geek, sep="\n")


def calculate_popularity() -> int:
    score = 0

    input_lines = map(str.rstrip, open(0))

    first_cond = r"^beegeek\b.*\bbeegeek$"
    second_cond = r"(^beegeek)|(beegeek$)"
    third_cond = r"beegeek"

    for line in input_lines:
        line = line.lower()
        if search(first_cond, line):
            score += 3
        elif search(second_cond, line):
            score += 2
        elif search(third_cond, line):
            score += 1

    return score


def greeting(text: str) -> bool:
    srch_regex = "^((Здравствуйте)|(Доброе утро)|(Добрый день)|(Добрый вечер))"
    srch_res = search(pattern=srch_regex, string=text, flags=re.I)

    if srch_res:
        return True
    return False


def count_beegeek(text: str) -> int:
    srch_regex = r".*beegeek.*"
    if re.search(pattern=srch_regex, string=text, flags=re.I):
        return 1
    return 0


if __name__ == "__main__":
    input_val = open(0)

    values = 0
    for line in input_val:
        values += count_beegeek(line)
    print(values)
