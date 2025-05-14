import os

# Token aus Railway Environment Variable holen
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# News-Abruf alle 60 Sekunden
FETCH_INTERVAL = 60  # Sekunden

# Alle Feeds + Channel-Zuordnung
RSS_FEEDS_CHANNELS = {
    "https://rss.app/feeds/6ylmybWwgG1OqovY.xml": 1371879824997744791,  # Trump News
    "https://rss.app/feeds/4NfbW8s5xqV7G7M4.xml": 1371879824997744791,  # Trump eigene Posts
    "https://www.n-tv.de/rss": 1371879772367622225,
    "https://rss.app/feeds/LHqcalDfUI6gqB33.xml": 1371879882258124840,
    "https://rss.app/feeds/BCVWNnbILyMc16Px.xml": 1371889076009177119,
    "https://rss.app/feeds/tTF0IKUt7fim3O2Q.xml": 1372274450652860476,
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best": 1372212944926015560,
    "https://feeds.marketwatch.com/marketwatch/bulletins/": 1372212944926015560,
    "https://www.cnbc.com/id/100003114/device/rss/rss.html": 1372212944926015560,
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US": 1372212944926015560,
    "https://feeds.oilprice.com/oilpricecom/BreakingNews": 1372212944926015560,
    "https://www.coindesk.com/arc/outboundfeeds/rss/": 1372212944926015560,
    "https://rss.app/feeds/4NfbW8s5xqV7G7M4.xml": 1371879824997744791,  # Trump's eigene Truth Social Posts
}
