import re


def multiple_split(string: str, delimiters: list[str]):
    delimiters_pattern = "|".join(map(re.escape, delimiters))

    return re.split(delimiters_pattern, string)


def sum_of_numbers(a: int, b: int, string: str):
    regex_for_numbers = re.compile(r"\d+")

    numbers = regex_for_numbers.findall(string, pos=a, endpos=b)
    print(numbers)
    return sum(map(int, numbers))


if __name__ == "__main__":
    a, b = map(int, input().split())
    string = input()
    print(sum_of_numbers(a, b, string))
