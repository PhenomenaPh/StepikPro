from typing import Any


def hash_function(obj: Any):
    trans_obj = str(obj)
    temp1, temp2 = 0, 0

    for i in range(len(trans_obj) // 2):
        temp1 += ord(trans_obj[i]) * ord(trans_obj[-i - 1])

    if len(trans_obj) % 2 != 0:
        temp1 += ord(trans_obj[len(trans_obj) // 2])

    for i, v in enumerate(trans_obj, start=1):
        temp2 += ord(v) * i * ((-1) ** (i + 1))

    final_result = (temp1 * temp2) % 123456791

    return final_result


def limited_hash(left: int, right: int, hash_function: callable = hash):
    width = right - left + 1

    def enhanced_hash(obj: Any):
        hash_val = hash_function(obj)

        if left <= hash_val <= right:
            pass
        else:
            offset = (hash_val - left) % width
            hash_val = left + offset

        return hash_val

    return enhanced_hash




