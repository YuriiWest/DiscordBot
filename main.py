import discord

client = discord.Client()
keywords = ["каеску", "кс"]


@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(1):
                await message.channel.send("щас бы коеску бавити")


client.run('')
