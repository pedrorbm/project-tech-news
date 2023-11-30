from tech_news.database import search_news
# from tech_news.scraper import scrape_news, fetch
import requests
from datetime import datetime


def search_by_title(title):
    MAIN_URL = "https://blog.betrybe.com/"
    result = []
    # requisition = scrape_news(fetch("https://blog.betrybe.com/"))
    try:
        notices = search_news({
            "title":
            {
                "$regex": title,
                "$options": "i"
            }
        })
        # requisition

        for notice in notices:
            MAIN_URL
            # requisition
            result.append((notice["title"], notice["url"]))

        # requisition["title"]
        MAIN_URL
    except requests.Timeout:
        return None

    return result


print(search_by_title("Algoritmos"))
print(search_by_title("games"))
print(search_by_title("favorites"))


def search_by_date(date):
    MAIN_URL = "https://blog.betrybe.com/"
    # requisition = scrape_news(fetch("https://blog.betrybe.com/"))
    result = []

    try:
        try:
            MAIN_URL
            day = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

            info = {"timestamp": day}

            MAIN_URL

            notices = search_news(info)

            result = [
                # requisition
                (new["title"], new["url"])
                for new in notices
            ]

            return result
        except ValueError:
            MAIN_URL
            raise ValueError("Data inválida")
    except requests.Timeout:
        return None


search_by_date("2021-04-04")
search_by_date("2047-02-10")


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
