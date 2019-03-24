import discord
import asyncio
import requests
from discord.ext import commands 
from discord.ext.commands import Bot

DISCORD_BOT_TOKEN = 'NTU4MzgzNDExMjk5ODc2ODc3.D3WCnA.LOOvdRr9QP6CaSiiVQu267_HJKg'

#class MyClient(discord.Client):

client = discord.Client()
Bot = commands.Bot(command_prefix= '!')

@Bot.event
async def on_ready():
    print('Bot is online')
    print('------')

@Bot.command(pass_context= True)
async def hello(ctx):
    """Hello =)"""
    await Bot.say ("Hello {}".format(ctx.message.author.mention) )


@Bot.command(pass_context= True)
async def info(ctx, user: discord.User):
    """Info about member"""
    emb = discord.Embed(title= "", colour= 0x00FF9900)
    emb.add_field(name= "Name :", value= user.name )
    emb.add_field(name= "Joined at: ", value= user.joined_at )
    emb.add_field(name= "Game :", value= user.game )
    emb.set_thumbnail(url= user.avatar_url)
    emb.set_author(name= Bot.user.name, url= user.avatar_url)
    emb.set_footer(text = "User id: {}".format(user.id), icon_url= user.avatar_url)
    await Bot.say(embed= emb)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def kick(ctx, member: discord.Member):
    """Use to kick"""
    await Bot.kick(member)

@Bot.command(pass_context= True)
async def ban(ctx, member: discord.Member, delete_message_days):
    """Use to ban"""
    await Bot.ban(member, delete_message_days)

@Bot.command(pass_context= True)
async def create_role(ctx):
    """Use to create role"""
    name_role = ' '.join(ctx.message.content.split(' ')[1:])
    server = ctx.message.server
    new_role = await Bot.create_role(server)
    await Bot.edit_role(server, new_role, name= name_role)

@Bot.command(pass_context= True)
async def add_role(ctx, user: discord.Member, role: discord.Role):
    """Use to add role"""
    await Bot.add_roles(user, role)

'''
@Bot.command(pass_context= True)
async def unban(ctx, user: discord.Member):
    await Bot.unban(user, ctx.message.server)
'''





Bot.run(DISCORD_BOT_TOKEN)