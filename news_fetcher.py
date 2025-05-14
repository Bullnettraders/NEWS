# news_fetcher.py

import feedparser

def fetch_news(rss_feeds):
    news = []
    for url in rss_feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            news.append({
                "title": entry.title,
                "link": entry.link,
                "source": url.split("//")[1].split("/")[0]  # z.B. reuters.com
            })
    return news
