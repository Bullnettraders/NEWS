import feedparser

def fetch_news(feed_url):
    feed = feedparser.parse(feed_url)
    news_items = []
    for entry in feed.entries[:5]:
        title = getattr(entry, "title", None)
        link = getattr(entry, "link", None)
        summary = getattr(entry, "summary", None)
        
        # Bild finden (optional)
        image = None
        if hasattr(entry, "media_content"):
            media = entry.media_content
            if isinstance(media, list) and len(media) > 0:
                image = media[0]['url']
        elif hasattr(entry, "media_thumbnail"):
            media = entry.media_thumbnail
            if isinstance(media, list) and len(media) > 0:
                image = media[0]['url']
        
        if title and link:
            news_item = {
                "title": title,
                "link": link,
                "source": feed_url,
                "summary": summary,
            }
            if image:
                news_item["image"] = image
            news_items.append(news_item)
    
    return news_items
