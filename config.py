import os

def safe_get_channel_id(var_name):
    value = os.getenv(var_name)
    if value is None:
        print(f"⚠️ Warnung: Umgebungsvariable '{var_name}' ist nicht gesetzt. Feed wird ignoriert.")
        return None
    try:
        return int(value)
    except ValueError:
        print(f"❌ Fehler: Umgebungsvariable '{var_name}' ist keine gültige Zahl.")
        return None

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    raise ValueError("Die Umgebungsvariable 'DISCORD_TOKEN' ist nicht gesetzt.")

FETCH_INTERVAL = 60  # Sekunden

# Kanal-IDs aus Umgebungsvariablen
channel_ntv = safe_get_channel_id("RSS_NTV")
channel_investing = safe_get_channel_id("RSS_INVESTING")
channel_watcher = safe_get_channel_id("RSS_WATCHER")
channel_times = safe_get_channel_id("RSS_TIMES")
channel_wirtschaft = safe_get_channel_id("RSS_WIRTSCHAFT")

# Feed-zu-Channel-Zuordnung nur, wenn die Variable gesetzt ist
RSS_FEEDS_CHANNELS = {}

if channel_ntv:
    RSS_FEEDS_CHANNELS.update({
        "https://www.n-tv.de/wirtschaft/rss": channel_ntv,
        "https://www.n-tv.de/politik/rss": channel_ntv,
    })

if channel_investing:
    RSS_FEEDS_CHANNELS["https://rss.app/feeds/LHqcalDfUI6gqB33.xml"] = channel_investing

if channel_watcher:
    RSS_FEEDS_CHANNELS["https://rss.app/feeds/BCVWNnbILyMc16Px.xml"] = channel_watcher

if channel_times:
    RSS_FEEDS_CHANNELS["https://rss.app/feeds/tTF0IKUt7fim3O2Q.xml"] = channel_times

if channel_wirtschaft:
    RSS_FEEDS_CHANNELS.update({
        "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best": channel_wirtschaft,
        "https://feeds.marketwatch.com/marketwatch/bulletins/": channel_wirtschaft,
        "https://www.cnbc.com/id/100003114/device/rss/rss.html": channel_wirtschaft,
        "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US": channel_wirtschaft,
        "https://feeds.oilprice.com/oilpricecom/BreakingNews": channel_wirtschaft,
        "https://www.coindesk.com/arc/outboundfeeds/rss/": channel_wirtschaft,
        "https://www.forbes.com/most-popular/feed/": channel_wirtschaft,
    })
