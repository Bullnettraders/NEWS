import feedparser

def fetch_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_items = []
    for entry in feed.entries[:5]:  # Nur die neuesten 5 Artikel
        news_items.append({
            "title": entry.title,
            "link": entry.link,
            "source": feed_url
        })
    return news_items
