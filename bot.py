import discord
from discord.ext import tasks, commands
import feedparser
from config import DISCORD_TOKEN, RSS_FEEDS_CHANNELS, FETCH_INTERVAL
from translator import translate_text

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

sent_entries = set()

@bot.event
async def on_ready():
    print(f"✅ Bot gestartet als {bot.user}")
    fetch_rss_feeds.start()

@tasks.loop(seconds=FETCH_INTERVAL)
async def fetch_rss_feeds():
    for feed_url, channel_id in RSS_FEEDS_CHANNELS.items():
        feed = feedparser.parse(feed_url)
        if feed.entries:
            for entry in feed.entries[:3]:  # nur die letzten 3 prüfen
                if entry.link not in sent_entries:
                    sent_entries.add(entry.link)
                    try:
                        channel = bot.get_channel(channel_id)
                        if channel:
                            # Titel übersetzen
                            title_de = translate_text(entry.title)

                            # Zusammenfassung prüfen und übersetzen
                            summary = getattr(entry, "summary", None)
                            if not summary:
                                summary = "Keine Vorschau verfügbar."

                            summary_de = translate_text(summary)

                            # Einheitliche Nachricht senden
                            nachricht = f"📰 **{title_de}**\n{summary_de}\n{entry.link}"
                            await channel.send(nachricht)
                        else:
                            print(f"❌ Kanal-ID {channel_id} nicht gefunden.")
                    except Exception as e:
                        print(f"❌ Fehler beim Senden an Kanal {channel_id}: {e}")

bot.run(DISCORD_TOKEN)
