import os

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

FETCH_INTERVAL = 60  # Sekunden

RSS_FEEDS_CHANNELS = {
    # Trump News
    "https://rss.politico.com/donald-trump.xml": 1371879824997744791,

    # n-tv News
    "https://www.n-tv.de/rss": 1371879772367622225,

    # Weitere Feeds
    "https://rss.app/feeds/LHqcalDfUI6gqB33.xml": 1371879882258124840,  # Investing
    "https://rss.app/feeds/BCVWNnbILyMc16Px.xml": 1371889076009177119,  # Watcher Guru
    "https://rss.app/feeds/tTF0IKUt7fim3O2Q.xml": 1372274450652860476,  # Times

    # Wirtschaftskanal
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best": 1372212944926015560,
    "https://feeds.marketwatch.com/marketwatch/bulletins/": 1372212944926015560,
    "https://www.cnbc.com/id/100003114/device/rss/rss.html": 1372212944926015560,
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US": 1372212944926015560,
    "https://feeds.oilprice.com/oilpricecom/BreakingNews": 1372212944926015560,
    "https://www.coindesk.com/arc/outboundfeeds/rss/": 1372212944926015560,
}
