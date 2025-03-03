import re


def word_count(word: str, sentence: str) -> int:
    srch_regex = rf"\B{word}\B"

    srch_count = len(re.findall(pattern=srch_regex, string=sentence))

    return srch_count


def american_word(word: str, sentence: str) -> int:
    srch_regex = rf"\b{word[:-2]}(se|ze)\b"

    srch_count = len(re.findall(pattern=srch_regex, string=sentence, flags=re.IGNORECASE))

    return srch_count


def abbreviate(phraze: str):
    srch_regex = r"\b\w|\B[A-Z]"
    srch_result = re.findall(pattern=srch_regex, string=phraze)

    return srch_result  # "".join(map(str.upper, srch_result))


def find_html_tag(string: str) -> str:
    srch_regex = r'href="(.*)">(.*?)</a>'
    srch_res = re.findall(pattern=srch_regex, string=string)

    if srch_res:
        return " ".join(srch_res[0])
    else:
        return None


if __name__ == "__main__":
    for line in open(0):
        line = line.strip()
        tags = find_html_tag(line)
        if tags:
            print(tags)
