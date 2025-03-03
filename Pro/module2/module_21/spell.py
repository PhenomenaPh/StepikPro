def spell(*words):

    if words:
        first_letters = set("".join([i[0] for i in words]))
        value_dict = {
            value.lower(): len(
                max((word for word in words if word[0] == value), key=len)
            )
            for value in first_letters
        }

        return value_dict
    else:
        return {}


words = ["Россия", "Австрия", "Австралия", "РумыниЯ", "Украина", "КИТай", "УЗБЕКИСТАН"]

print(spell(*words))
