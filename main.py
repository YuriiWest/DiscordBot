import discord

client = discord.Client()
keywords = ["каеску", "кс"]


@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(1):
                await message.channel.send("щас бы каеску бавити")


client.run('ODE3MzkyNzA2Nzk5MTQwOTE1.YEI2Rw.CT3-r7vMg0rQw-FJ-_zC_os6xhs')
