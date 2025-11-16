import os

# --- Hilfsfunktion zur robusten Laden der Kanal-IDs ---
def sichere_kanal_id(var_name):
    """
    Lädt eine Kanal-ID aus den Umgebungsvariablen.
    Gibt 'None' zurück, wenn die Variable nicht gesetzt oder ungültig ist.
    """
    wert = os.getenv(var_name)
    
    # Fall 1: Variable ist nicht gesetzt
    if wert is None:
        print(f"⚠️ Hinweis: Die Umgebungsvariable '{var_name}' ist nicht gesetzt. Dieser Feed wird übersprungen.")
        return None
    
    # Fall 2: Variable ist gesetzt, aber keine gültige Zahl
    try:
        return int(wert)
    except ValueError:
        print(f"❌ Fehler: Die Umgebungsvariable '{var_name}' muss eine gültige Zahl (Channel ID) sein. Wert war: '{wert}'")
        return None

# --- 1. Bot-Konfiguration laden ---

# DISCORD_TOKEN (Muss vorhanden sein, sonst Abbruch)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    raise ValueError("❌ Die Umgebungsvariable 'DISCORD_TOKEN' ist nicht gesetzt. Bitte in Railway hinzufügen.")

# Intervall für das Abrufen der Feeds (in Sekunden)
FETCH_INTERVAL = 60  

# --- 2. Kanal-IDs sicher laden ---
print("Lade Kanal-Konfigurationen...")
kanal_ntv = sichere_kanal_id("RSS_NTV")
kanal_finanzen = sichere_kanal_id("RSS_FINANZEN")  
kanal_watcher = sichere_kanal_id("RSS_WATCHER")
kanal_times = sichere_kanal_id("RSS_TIMES")
kanal_wirtschaft = sichere_kanal_id("RSS_WIRTSCHAFT")

# --- 3. RSS-Feed-Liste dynamisch aufbauen ---
# Das Haupt-Dictionary, das alle Feeds und ihre Zielkanäle enthält
RSS_FEEDS_CHANNELS = {}

if kanal_ntv:
    RSS_FEEDS_CHANNELS.update({
        "https://www.n-tv.de/wirtschaft/rss": kanal_ntv,
        "https://www.n-tv.de/politik/rss": kanal_ntv,
    })

if kanal_finanzen:
    RSS_FEEDS_CHANNELS["https://www.finanzen.net/rss/news"] = kanal_finanzen

if kanal_watcher:
    RSS_FEEDS_CHANNELS["https://nitter.net/WatcherGuru/rss"] = kanal_watcher

if kanal_times:
    RSS_FEEDS_CHANNELS["https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"] = kanal_times

if kanal_wirtschaft:
    RSS_FEEDS_CHANNELS.update({
        "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best": kanal_wirtschaft,
        "https://feeds.marketwatch.com/marketwatch/bulletins/": kanal_wirtschaft,
        # Korrigierter CNBC-Feed
        "https://www.cnbc.com/id/19746125/device/rss/rss.html": kanal_wirtschaft, 
        "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^DJI&region=US&lang=en-US": kanal_wirtschaft,
        "https://feeds.oilprice.com/oilpricecom/BreakingNews": kanal_wirtschaft,
        "https://www.coindesk.com/arc/outboundfeeds/rss/": kanal_wirtschaft,
        # Korrigierter Forbes-Feed
        "https://www.forbes.com/news/feed/": kanal_wirtschaft,
    })

# --- 4. Abschluss der Konfiguration ---
if not RSS_FEEDS_CHANNELS:
    print("⚠️ WICHTIG: Keine RSS-Umgebungsvariablen (z.B. 'RSS_NTV') gefunden.")
    print("Der Bot wird starten, aber keine Feeds abrufen.")
else:
    print(f"✅ Konfiguration erfolgreich. {len(RSS_FEEDS_CHANNELS)} Feeds werden überwacht.")

print("-" * 30)

# (Hier beginnt der restliche Code deines Bots, z.B. discord.py Imports)
