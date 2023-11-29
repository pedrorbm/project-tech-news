import requests
import time
from parsel import Selector
from tech_news.database import create_news


def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )

        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


def scrape_updates(html_content):
    result = []
    selector = Selector(text=html_content)

    for element in selector.css(".cs-overlay"):
        a = element.css("a::attr(href)").get()
        result.append(a)

    return result


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    result = selector.css(".next::attr(href)").get()

    return result


def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date ::text").get()
    writer = selector.css("span.author a::text").get().strip()
    reading_time = selector.css(".meta-reading-time ::text").get()[:2]
    summary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    category = selector.css(".label ::text").get()

    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }

    return result


# html = fetch("https://blog.betrybe.com/tecnologia/modelo-as-a-service/")
# print(scrape_news(html))


def get_tech_news(amount):
    try:
        MAIN_URL = "https://blog.betrybe.com/"
        cards = scrape_updates(MAIN_URL)
        next = scrape_next_page_link(MAIN_URL)
        data = []

        while len(data) < amount:
            cards
            scrape_updates(MAIN_URL)
            data.extend(scrape_updates(fetch(MAIN_URL)))
            next
            scrape_next_page_link(MAIN_URL)
            MAIN_URL = scrape_next_page_link(fetch(MAIN_URL))

        scrape_next_page_link(MAIN_URL)
        result = [scrape_news(fetch(card)) for card in data[:amount]]
        scrape_updates(MAIN_URL)
        cards
        next

        create_news(result)

        return result
    except requests.Timeout:
        return None
