import os

def sichere_kanal_id(var_name):
    wert = os.getenv(var_name)
    if wert is None:
        print(f"⚠️ Hinweis: Die Umgebungsvariable '{var_name}' ist nicht gesetzt. Dieser Feed wird übersprungen.")
        return None
    try:
        return int(wert)
    except ValueError:
        print(f"❌ Fehler: Die Umgebungsvariable '{var_name}' muss eine gültige Zahl sein.")
        return None

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    raise ValueError("❌ Die Umgebungsvariable 'DISCORD_TOKEN' ist nicht gesetzt. Bitte in Railway hinzufügen.")

FETCH_INTERVAL = 60  # Sekunden

kanal_ntv = sichere_kanal_id("RSS_NTV")
kanal_investing = sichere_kanal_id("RSS_INVESTING")
kanal_watcher = sichere_kanal_id("RSS_WATCHER")
kanal_times = sichere_kanal_id("RSS_TIMES")
kanal_wirtschaft = sichere_kanal_id("RSS_WIRTSCHAFT")

RSS_FEEDS_CHANNELS = {}

if kanal_ntv:
    RSS_FEEDS_CHANNELS.update({
        "https://www.n-tv.de/wirtschaft/rss": kanal_ntv,
        "https://www.n-tv.de/politik/rss": kanal_ntv,
    })

if kanal_investing:
    RSS_FEEDS_CHANNELS["https://rss.app/feeds/LHqcalDfUI6gqB33.xml"] = kanal_investing

if kanal_watcher:
    RSS_FEEDS_CHANNELS["https://rss.app/feeds/BCVWNnbILyMc16Px.xml"] = kanal_watcher

if kanal_times:
    RSS_FEEDS_CHANNELS["https://rss.app/feeds/tTF0IKUt7fim3O2Q.xml"] = kanal_times

if kanal_wirtschaft:
    RSS_FEEDS_CHANNELS.update({
        "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best": kanal_wirtschaft,
        "https://feeds.marketwatch.com/marketwatch/bulletins/": kanal_wirtschaft,
        "https://www.cnbc.com/id/100003114/device/rss/rss.html": kanal_wirtschaft,
        "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US": kanal_wirtschaft,
        "https://feeds.oilprice.com/oilpricecom/BreakingNews": kanal_wirtschaft,
        "https://www.coindesk.com/arc/outboundfeeds/rss/": kanal_wirtschaft,
        "https://www.forbes.com/most-popular/feed/": kanal_wirtschaft,
    })
