import os
from re import A
from turtle import title
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv(verbose=True)

TOKEN = os.getenv('token')

pomoci = commands.Bot(command_prefix="p!", intents = discord.Intents.all())

print("STARTED")


@pomoci.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, reason = None):
    #delete message
    await ctx.message.delete()
    
    
    #embed
    kickemd = discord.Embed(title = "kicked" , description = f"{user.mention}  was kicked by {ctx.author.mention} + \n reason:  + " + reason)
    await ctx.channel.send(embed=kickemd)
    
    #kick user
    await user.kick()


@pomoci.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason = None):
    #delete message
    await ctx.message.delete()
    
    banemd = discord.Embed(title = "banned" , description = f"{user.mention}  was banned by {ctx.author.mention}  \n reason:    **{reason}**")
    await ctx.channel.send(embed=banemd)
    await user.ban()

@pomoci.command(name="unban", help="command to unban user")
@commands.has_permissions(administrator=True)
async def _unban(ctx, *, member_id: int):
    """ command to unban user. check !help unban """
    await ctx.guild.unban(discord.Object(id=member_id))
    unbanemd = discord.Embed(title = "Unban", description = f"{member_id}  was unbanned  by {ctx.author.mention} ")
    await ctx.send(embed=unbanemd)



    
    
    
    


pomoci.run(TOKEN)


