import os

def get_channel_id(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Umgebungsvariable '{var_name}' ist nicht gesetzt.")
    return int(value)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    raise ValueError("Die Umgebungsvariable 'DISCORD_TOKEN' ist nicht gesetzt.")

FETCH_INTERVAL = 60  # Sekunden

# Kanal-IDs aus Umgebungsvariablen
channel_ntv = get_channel_id("RSS_NTV")
channel_investing = get_channel_id("RSS_INVESTING")
channel_watcher = get_channel_id("RSS_WATCHER")
channel_times = get_channel_id("RSS_TIMES")
channel_wirtschaft = get_channel_id("RSS_WIRTSCHAFT")

# Feed-zu-Channel-Zuordnung
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
