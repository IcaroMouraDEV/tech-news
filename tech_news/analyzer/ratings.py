from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    """Seu código deve vir aqui"""
    raw_data = Counter([new['category'] for new in find_news()])
    data = sorted(raw_data.items(), key=lambda a: (-a[1], a[0]))
    print(data)

    return [category[0] for category in data][:5]
