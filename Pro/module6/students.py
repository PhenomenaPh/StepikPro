from collections import Counter
from sys import stdin

students = stdin.read().splitlines()
stundets_cnt = Counter({student: int(score) for student, score in map(str.split, students)})
print(stundets_cnt.most_common()[-2][0])
