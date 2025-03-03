news_list = [news.strip().split(" / ") if "/" in news else news for news in open(0)]
category = news_list.pop()

sorted_news = [
    news[0]
    for news in sorted(
        filter(lambda x: x[1] == category, news_list),
        key=lambda x: (float(x[2]), x[0]),
    )
]
print(*sorted_news, sep="\n")
