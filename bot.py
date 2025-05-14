# bot.py

import discord
import asyncio
from config import DISCORD_TOKEN, RSS_FEEDS, FETCH_INTERVAL
from news_fetcher import fetch_news
from translator import translate_text
from deduplicator import is_new
from poster import post_news

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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

@client.event
async def on_ready():
    print(f'{client.user} ist online und postet News.')

client.loop.create_task(news_loop())
client.run(DISCORD_TOKEN)
