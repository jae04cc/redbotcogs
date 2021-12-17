import discord
from redbot.core import Config, checks, commands

class threadmanager(commands.Cog):
    """
    An OK thread manager
    """

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
    
    @commands.Cog.listener
    async def on_message(self, message: discord.Message):
        if message.content.startswith('oh hai mark'):
            await message.channel.send('oh hai johnny')