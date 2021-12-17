from redbot.core import commands

class threadmanager(commands.Cog):
    """My custom cog: threadmanager"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def thread(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")