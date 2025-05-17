import discord
from config import DISCORD_TOKEN

client = discord.Client()

@client.event
async def _on_ready():
    print("Hello from AniMate!!!")

client.run(DISCORD_TOKEN, reconnect=True)