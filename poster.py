import discord
from translator import translate_text

async def post_news(news_item, client, channel_id):
    channel = client.get_channel(channel_id)
    if channel:
        # Breaking News Detection
        title_text = news_item["title"].lower()
        is_breaking = "breaking" in title_text or "eilmeldung" in title_text or "urgent" in title_text

        embed_color = discord.Color.red() if is_breaking else discord.Color.blue()

        # Titel ins Deutsche übersetzen
        translated_title = translate_text(news_item["title"])

        # Summary übersetzen, wenn vorhanden
        translated_summary = None
        if "summary" in news_item and news_item["summary"]:
            translated_summary = translate_text(news_item["summary"])

        embed = discord.Embed(
            title=translated_title,
            description=f"[👉 Hier klicken zur Quelle]({news_item['link']})",
            color=embed_color
        )

        if translated_summary:
            embed.add_field(name="Zusammenfassung", value=translated_summary[:200] + "...", inline=False)

        if "image" in news_item and news_item["image"]:
            embed.set_thumbnail(url=news_item["image"])

        await channel.send(embed=embed)
