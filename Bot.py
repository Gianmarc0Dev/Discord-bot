import discord#----------------------------------------------pip install discord
from discord.ext import commands

TOKEN = "your bot token"

bot = commands.Bot(command_prefix="/")#----------------------your command prefix

@bot.command()
async def say(ctx, word):#-----------------------------------the name of the function is also the name of the command the second parameter
  await ctx.send(word)#--------------------------------------of the function is from the message for example:/say hello! the bot will respond "hello"

@bot.command(name="your command name")#-----------------------if you want a different name for the command use the parameter name
async def example_function(ctx):#----------------------------and call the function with the name you want
  return

bot.run(TOKEN)#----------------------------------------------run the bot using the token

#made by Gianmarco with love <3
