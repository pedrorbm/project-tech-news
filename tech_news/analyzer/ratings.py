import requests
from collections import Counter
# from tech_news.scraper import scrape_news, fetch
from tech_news.database import search_news


def top_5_categories():
    MAIN_URL = "https://blog.betrybe.com/"
    array = list()

    try:
        try:
            # requisition = scrape_news(fetch("https://blog.betrybe.com/"))
            array = list()
            MAIN_URL = "https://blog.betrybe.com/"
            dic = dict()
            MAIN_URL
            notices = Counter(
                notice["category"]
                for notice in search_news(dic)
            )
            # requisition
            MAIN_URL
            array

            selected = sorted(
                # requisition
                notices.keys(),
                key=lambda
                category: (-notices[category], category)
                )

            # requisition
            array
            result = selected
            MAIN_URL

            return result[:5]
        except requests.Timeout:
            return "Error"
    except requests.Timeout:
        return None
