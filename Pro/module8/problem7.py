def recursion_len_digit(nums: str):
    if not nums:
        return 0
    else:
        return 1 + recursion_len_digit(nums[1:])


def recursion_len_digit_v2(num: int):
    if num < 10:
        return 1
    else:
        return 1 + recursion_len_digit_v2(num // 10)

print(recursion_len_digit_v2(int(input())))