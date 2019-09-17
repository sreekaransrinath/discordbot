import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k.') #You can add any prefix here

discord_token = input("Enter your discord token ") 

#Checking if the script has started running successfully
@client.event 
async def on_ready():
    print("Ready to rumble")

#Client Latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

#Purging Messages
@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

#Kick
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'Successfully kicked member')

#Ban
@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

#This function replies to a "Hello" message with a "Hello"
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(discord_token)
