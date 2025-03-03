from collections import ChainMap


def get_all_values(chainmap: ChainMap[str, str], key: str) -> set:
    if key:
        values = set(i[key] for i in chainmap.maps if key in i)
    else:
        values = set()

    return values
