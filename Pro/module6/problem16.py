from collections import ChainMap


def get_value(chainmap: ChainMap[str, str], key: str, from_left: bool = True) -> str | None:
    if from_left:
        return chainmap.get(key)
    else:
        # Get key from reverse order
        for mapping in reversed(chainmap.maps):
            if key in mapping:
                return mapping[key]
    return None
