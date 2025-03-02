from datetime import date
from typing import List


def sorted_dates(dates: List[date]) -> List[date]:
    return [value.strftime("%d/%m/%Y") for value in sorted(dates)]


if __name__ == "__main__":
    init_dates = [date.fromisoformat(input()) for value in range(int(input()))]
    print(*sorted_dates(init_dates), sep="\n")
