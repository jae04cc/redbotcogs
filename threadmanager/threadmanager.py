import discord
from discord.http import Route
from redbot.core import Config, checks, commands

async def create_thread(bot, channel: discord.TextChannel, message: discord.Message, name: str, archive: int = 4320):
    """
    Creates a new thread in the channel from the message
    Args:
        channel (TextChannel): The channel the thread will be apart of
        message (Message): The discord message the thread will start with
        name (str): The name of the thread
        archive (int): The archive duration. Can be 60, 1440, 4320, and 10080.
    Returns:
        int: The channel ID of the newly created thread
    """
    guild = channel.guild
    if archive > 4320 and "THREE_DAY_THREAD_ARCHIVE" not in guild.features:
        archive = 1440
    elif archive == 10080 and "SEVEN_DAY_THREAD_ARCHIVE" not in guild.features:
        archive = 4320

    fields = {"name": name, "auto_archive_duration": archive}
    reason = "Thread Manager"

    r = Route(
        "POST",
        "/channels/{channel_id}/messages/{message_id}/threads",
        channel_id=channel.id,
        message_id=message.id,
    )

    return (await bot.http.request(r, json=fields, reason=reason))["id"]

class ThreadManager(commands.Cog):
    """
    Better Thread Manager
    """

    def __init__(self, bot):
        self.bot = bot

    async def thread(self, ctx, *, name: str):
        """
        Create a new thread from this channel
        You must have proper permissions set
        """
        channel = ctx.channel
        guild = ctx.guild
        user = ctx.author

        await create_thread(self.bot, channel, ctx.message, name=name, archive=archive)