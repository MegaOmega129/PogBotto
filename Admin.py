import nextcord, json, os, sys
from nextcord.ext import commands

class Admin(commands.Cog):
    """The Admin Commands"""
    def __init__(self, bot:commands.Bot):
        self.bot = bot

#kick
    @commands.command(name = "Kick")
    async def Kick(self, ctx:commands.Context, user:nextcord.Member, reason:str = "Kicked by admins"):
        await ctx.guild.kick(user, reason = reason)
        await ctx.send(f"{user.name} was kicked for {reason}")

#purge
    @commands.command(name = "purge")
    async def purge(self, ctx:commands.Context, messages:int = 50):
        await ctx.channel.purge(limit = messages)
        embed=nextcord.Embed(color=0x1f6cd1)
        embed.add_field(name="Purge", value="Purged this channel", inline=False)
        await ctx.send(embed=embed)
   
    @commands.command(name = "Ban")
    async def ban(self, ctx:commands.Context, user:nextcord.Member, reason:str = "Bannned by admins"):
      await ctx.guild.ban(user, reason = reason)
      await ctx.send(f"{user.name} was banned for {reason}")

#setup module
def setup(Bot:commands.Bot):
  Bot.add_cog(Admin(Bot))