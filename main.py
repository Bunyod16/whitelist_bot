from discord.ext import commands
from commands import general_commands
from utils import get_token

PREFIX = ("!")
bot = commands.Bot(command_prefix=PREFIX, description='Hi', help_command=None)

@bot.event
async def on_ready():
    global mention_string
    global SERVER_ID
    global MENTION_ROLE_NAMES

    print(bot.user.name, "is online")
    print(bot.user.id)

@bot.command(pass_context = True)
async def clear(ctx, number):
  if (ctx.author.id == 237063450646282241):
      mgs = [] #Empty list to put all the messages in the log
      number = int(number) #Converting the amount of messages to delete to an integer
      async for x in ctx.message.channel.history(limit = number):
        await x.delete()
      print(mgs)
  
bot.add_cog(general_commands())
bot.run(get_token())
