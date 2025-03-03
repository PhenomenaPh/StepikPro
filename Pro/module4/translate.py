tr_str = input()
actual_str = input().lower()
english_alphabets = "abcdefghijklmnopqrstuvwxyz"


tr_str_table = str.maketrans(english_alphabets, tr_str)
print(actual_str.translate(tr_str_table))