from collections import ChainMap


def deep_update(chainmap: ChainMap[str, str], key: str, value: str) -> None:
    if key not in chainmap:
        chainmap[key] = value
    else:
        for mapping in chainmap.maps:
            if key in mapping:
                mapping[key] = value
                break
