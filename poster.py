import discord

async def post_news(news_item, client, channel_id):
    channel = client.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title=f"🚨 {news_item['translated_title']}",
            description=f"[Zur Quelle]({news_item['link']})",
            color=discord.Color.blue()
        )
        await channel.send(embed=embed)
