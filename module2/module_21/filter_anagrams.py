def filter_anagrams(word: str, words: list):

    sorted_word = "".join(sorted(word))

    return [i for i in words if sorted_word == "".join(sorted(i))]
