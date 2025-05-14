import discord
import asyncio
import datetime
import os
from config import DISCORD_TOKEN, RSS_FEEDS_CHANNELS, FETCH_INTERVAL
from news_fetcher import fetch_news
from translator import translate_text
from deduplicator import is_new
from poster import post_news
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

keep_alive()

@client.event
async def on_ready():
    print(f'{client.user} ist online und postet News.')

async def news_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        for feed_url, channel_id in RSS_FEEDS_CHANNELS.items():
            news_list = fetch_news(feed_url)
            for news_item in news_list:
                if is_new(news_item):
                    translated_title = translate_text(news_item["title"])
                    news_item["translated_title"] = translated_title
                    await post_news(news_item, client, channel_id)
        await asyncio.sleep(FETCH_INTERVAL)

async def moo_moc_alerts():
    await client.wait_until_ready()
    sent_today_open = False
    sent_today_close = False

    while not client.is_closed():
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=2)  # UTC+2

        if now.hour == 15 and now.minute == 0 and not sent_today_open:
            for channel_id in set(RSS_FEEDS_CHANNELS.values()):
                channel = client.get_channel(channel_id)
                if channel:
                    await channel.send("🔔 Nasdaq 100 (NQ) Market Open: Achte auf MOO-Volumen!")
            sent_today_open = True

        if now.hour == 21 and now.minute == 30 and not sent_today_close:
            for channel_id in set(RSS_FEEDS_CHANNELS.values()):
                channel = client.get_channel(channel_id)
                if channel:
                    await channel.send("🔔 Nasdaq 100 (NQ) Market Close: Achte auf MOC-Volumen!")
            sent_today_close = True

        if now.hour == 0 and now.minute == 0:
            sent_today_open = False
            sent_today_close = False

        await asyncio.sleep(30)

client.loop.create_task(news_loop())
client.loop.create_task(moo_moc_alerts())

client.run(DISCORD_TOKEN)
