import discord
from redbot.core import Config, checks, commands
import requests

async def create_thread(self,name,minutes,message):
    token = 'Bot ' + self._state.http.token
    url = f"https://discord.com/api/v9/channels/{self.id}/messages/{message.id}/threads"
    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    data = {
        "name" : name,
        "type" : 11,
        "auto_archive_duration" : minutes
    }
 
    return requests.post(url,headers=headers,json=data).json()

discord.TextChannel.create_thread = create_thread
Bot = discord.Client()
 
@Bot.event
async def on_message(ctx):
    if ctx.content == "?thread":
        f = await ctx.channel.create_thread(name="Thread", minutes=4320, message=ctx)
Bot.run("token")