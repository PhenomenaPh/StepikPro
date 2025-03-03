def similar_words():
    base_words = input()
    good_letters = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е"]
    good_indexes = [
        index for index, value in enumerate(base_words) if value in good_letters
    ]

    for _ in range(int(input())):
        word = input()

        word_indexes = [
            index
            for index, letter in enumerate(word[: len(base_words) + 1])
            if letter in good_letters
        ]

        if good_indexes == word_indexes:
            print(word)


similar_words()
