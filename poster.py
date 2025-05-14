import discord

async def post_news(news_item, client, channel_id):
    channel = client.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title=news_item["title"],
            description=f"[👉 Hier klicken zur Quelle]({news_item['link']})",
            color=discord.Color.blue()
        )

        if "summary" in news_item and news_item["summary"]:
            embed.add_field(name="Zusammenfassung", value=news_item["summary"][:200] + "...", inline=False)

        if "image" in news_item and news_item["image"]:
            embed.set_thumbnail(url=news_item["image"])

        await channel.send(embed=embed)
