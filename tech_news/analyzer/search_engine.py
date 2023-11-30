from tech_news.database import search_news
# from tech_news.scraper import scrape_news, fetch
import requests


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


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
