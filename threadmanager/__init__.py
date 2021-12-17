from .threadmanager import threadmanager


def setup(bot):
    bot.add_cog(threadmanager(bot))