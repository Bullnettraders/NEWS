# poster.py

import discord
from config import CHANNEL_ID

async def post_news(news_item, client):
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="🚨 [BREAKING] " + news_item["translated_title"],
            description=f"Quelle: {news_item['source']}\n[Link zur News]({news_item['link']})",
            color=discord.Color.red()
        )
        await channel.send(embed=embed)
