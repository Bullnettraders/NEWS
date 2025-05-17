import discord
from discord.ext import tasks, commands
import feedparser
from config import DISCORD_TOKEN, RSS_FEEDS_CHANNELS, FETCH_INTERVAL

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Speicher bereits gesendeter Links
sent_entries = set()

@bot.event
async def on_ready():
    print(f"Bot ist eingeloggt als {bot.user}")
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
                            await channel.send(f"📰 **{entry.title}**\n{entry.link}")
                        else:
                            print(f"Kanal mit ID {channel_id} nicht gefunden.")
                    except Exception as e:
                        print(f"Fehler beim Senden an Kanal {channel_id}: {e}")

bot.run(DISCORD_TOKEN)
