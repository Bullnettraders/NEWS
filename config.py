import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

FETCH_INTERVAL = 60  # Sekunden

# Kanal-IDs aus Umgebungsvariablen laden
channel_ntv = int(os.getenv("RSS_NTV"))
channel_investing = int(os.getenv("RSS_INVESTING"))
channel_watcher = int(os.getenv("RSS_WATCHER"))
channel_times = int(os.getenv("RSS_TIMES"))
channel_wirtschaft = int(os.getenv("RSS_WIRTSCHAFT"))

RSS_FEEDS_CHANNELS = {
    # n-tv Feed
    "https://www.n-tv.de/wirtschaft/rss": channel_ntv,
    "https://www.n-tv.de/politik/rss": channel_ntv,

    # Investing
    "https://rss.app/feeds/LHqcalDfUI6gqB33.xml": channel_investing,

    # Watcher Guru
    "https://rss.app/feeds/BCVWNnbILyMc16Px.xml": channel_watcher,

    # Times
    "https://rss.app/feeds/tTF0IKUt7fim3O2Q.xml": channel_times,

    # Wirtschaftskanal
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best": channel_wirtschaft,
    "https://feeds.marketwatch.com/marketwatch/bulletins/": channel_wirtschaft,
    "https://www.cnbc.com/id/100003114/device/rss/rss.html": channel_wirtschaft,
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US": channel_wirtschaft,
    "https://feeds.oilprice.com/oilpricecom/BreakingNews": channel_wirtschaft,
    "https://www.coindesk.com/arc/outboundfeeds/rss/": channel_wirtschaft,
    "https://www.forbes.com/most-popular/feed/": channel_wirtschaft,
}
