import discord

async def post_news(news_item, client, channel_id):
    channel = client.get_channel(channel_id)
    if channel:
        embed = discord.Embed(
            title=f"{news_item['translated_title']}",
            description=f"[Zur Quelle]({news_item['link']})",
            color=discord.Color.blue()
        )
        
        # Bild hinzufügen, wenn verfügbar
        if 'image' in news_item:
            embed.set_thumbnail(url=news_item['image'])

        # Summary hinzufügen, wenn verfügbar
        if 'summary' in news_item:
            embed.add_field(name="Zusammenfassung", value=news_item['summary'], inline=False)
        
        await channel.send(embed=embed)
