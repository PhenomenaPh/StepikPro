def bad_translate():

    languages = [set(input().split(", ")) for i in range(int(input()))]

    lang_speaking = set.intersection(*languages)

    if lang_speaking:
        print(*sorted(lang_speaking), sep=", ")
    else:
        print("Сериал снять не удастся")


bad_translate()
