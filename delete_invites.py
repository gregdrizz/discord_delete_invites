import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= '?')

@client.event
async def on_ready():
    print("We have loggged in as {0.user}".format(client))

@client.command()
@commands.has_permissions(administrator=True)
async def deleteinvites(ctx):
    await ctx.send("Started deleting successfuly")
    for invite in await ctx.guild.invites():
        print(invite)
        await invite.delete() 
    await ctx.send("Invites deleted successfuly")

client.run(DISCORD_TOKEN)