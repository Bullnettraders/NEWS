import discord
import asyncio
import datetime
from config import DISCORD_TOKEN, RSS_FEEDS, FETCH_INTERVAL
from news_fetcher import fetch_news
from translator import translate_text
from deduplicator import is_new
from poster import post_news
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)   # <--- CLIENT wird HIER erstellt

keep_alive()  # Webserver starten (damit Railway nicht stopt)

@client.event
async def on_ready():
    print(f'{client.user} ist online und postet News.')

async def news_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        news_list = fetch_news(RSS_FEEDS)
        for news_item in news_list:
            if is_new(news_item):
                translated_title = translate_text(news_item["title"])
                news_item["translated_title"] = translated_title
                await post_news(news_item, client)
        await asyncio.sleep(FETCH_INTERVAL)

async def moo_moc_alerts():
    await client.wait_until_ready()
    sent_today_open = False
    sent_today_close = False

    while not client.is_closed():
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # UTC+2 für Sommerzeit

        if now.hour == 15 and now.minute == 0 and not sent_today_open:
            channel = client.get_channel(int(os.getenv("CHANNEL_ID")))
            if channel:
                await channel.send("🔔 Nasdaq 100 (NQ) Market Open: Achte auf MOO-Volumen!")
                sent_today_open = True
            else:
                print("Fehler: Channel nicht gefunden!")

        if now.hour == 21 and now.minute == 30 and not sent_today_close:
            channel = client.get_channel(int(os.getenv("CHANNEL_ID")))
            if channel:
                await channel.send("🔔 Nasdaq 100 (NQ) Market Close: Achte auf MOC-Volumen!")
                sent_today_close = True
            else:
                print("Fehler: Channel nicht gefunden!")

        if now.hour == 0 and now.minute == 0:
            sent_today_open = False
            sent_today_close = False

        await asyncio.sleep(30)

# Beide Aufgaben gleichzeitig starten
client.loop.create_task(news_loop())
client.loop.create_task(moo_moc_alerts())

client.run(DISCORD_TOKEN)
