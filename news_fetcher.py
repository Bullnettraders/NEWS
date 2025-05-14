import feedparser

def fetch_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_items = []
    for entry in feed.entries[:5]:  # Nur die neuesten 5 Artikel
        title = getattr(entry, "title", None)
        link = getattr(entry, "link", None)
        if title and link:  # Nur wenn beides existiert
            news_items.append({
                "title": title,
                "link": link,
                "source": feed_url
            })
    return news_items
