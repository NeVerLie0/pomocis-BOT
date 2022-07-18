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
async def unban(ctx, *, member_id: int):
    """ command to unban user. check !help unban """
    await ctx.guild.unban(discord.Object(id=member_id))
    unbanemd = discord.Embed(title = "Unban", description = f"{member_id}  was unbanned  by {ctx.author.mention} ")
    await ctx.send(embed=unbanemd)



@pomoci.command()
async def ce(ctx):
    def check(message):
      return message.author == ctx.author and message.channel == ctx.channel
    

    
    await ctx.send('Enter your title.\nPut `none` if you do not want anything in this section.')
    title = await pomoci.wait_for("message", timeout = 300.0, check=check)
    title = title.content
    if title == "none":
      title = "** **" # it will still be empty but not give an empty error message
    else:
      title = title

    
    await ctx.send('Enter your title.\nPut `none` if you do not want anything in this section.')
    desc = await pomoci.wait_for("message", timeout = 300.0, check=check)
    desc = desc.content
    if desc == "none":
      desc = "** **"
    else:
      desc = desc

    embed = discord.Embed(title=title, description=desc, color=0xa9e9e9)
    await ctx.send(embed=embed)



    
    
    
    


pomoci.run(TOKEN)


