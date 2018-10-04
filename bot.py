import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='aqua ')
ownerID = "329337654850093056"

# To remove the help command and make your own help command
#bot.remove_command('help')

@bot.event
async def on_ready():
  print ("------")
  print ("My name is " + bot.user.name)
  print ("With the ID: " + bot.user.id)
  print ("Using discord.py v" + discord.__version__)
  print ("------")
  
  # Make me say stuff
@bot.command(pass_context=True)
async def say(ctx, *args):
    """Make me say your message"""
    if ctx.message.author.id in ownerID:
        channel = ctx.message.channel
        mesg = ' '.join(args)
        await bot.delete_message(ctx.message)
        await bot.send_typing(channel)
        await asyncio.sleep(1)
        await bot.say(mesg)
        print (ctx.message.author.id + " or " + ctx.message.author.name + " made me say '{}'".format(mesg))
    else:
      await bot.say("You are not allowed to run this command!")
      
@bot.command(pass_context=True)
async def kill(ctx, user: discord.Member=None):
        if user is None:
            await bot.say(ctx.message.author.mention + ": I can't kill anyone unless you tell me who to kill!")
            return
        if user.id == "490915177940647936":
            await bot.say(ctx.message.author.mention + ": I won't let you kill me! :knife:")
        elif user.id == ownerID:
            await bot.say(ctx.message.author.mention + " I dont wanna kill him, hes my onii-chan.")
        if user.id == "274298631517896704":
            await bot.say(ctx.message.author.mention + "I dont wanna kill him! Hes the reason I exist!")
        elif user.id == ctx.message.author.id:
            await bot.say(ctx.message.author.mention + ": Why do you want me to kill you?")
        else:
            await bot.say("I have killed {}".format(user.name))

@bot.command(pass_context=True)
async def waifu(ctx):
  await bot.say("I am Xenzai's waifu")
  
@bot.command(pass_context=True)
async def playing(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= (mesg)))
    await bot.say("I am now playing " + mesg)
    
@bot.command(pass_context=True)
async def watching(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=3))
    
@bot.command(pass_context=True)
async def listening(ctx, *args):
  if ctx.message.author.id in ownerID:
    mesg = ' '.join(args)
    await bot.change_presence(game=discord.Game(name= mesg, type=2))
    


bot.run(os.environ.get('Token'))
