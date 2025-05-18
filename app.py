import discord
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def _on_ready():
    print("Hello from AniMate!!!")

client.run(DISCORD_TOKEN, reconnect=True)