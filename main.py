import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k.')

discord_token = input("Enter your discord token ")

@client.event
async def on_ready():
    print("Ready to rumble")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'Successfully kicked member')

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(discord_token)
