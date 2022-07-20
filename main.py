import asyncio
import os
from pydoc import describe
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

@pomoci.command()
async def delc(ctx):
    def check(message):
      return message.author == ctx.author and message.channel == ctx.channel
    await ctx.channel.delete()

#embed for dhm
one = discord.Embed(title="DM HELP", description  ="Type what u need help for we will dm You")
two = discord.Embed(title="is that all? ")
@pomoci.command()
async def dmh(ctx):
    num = 1
    await ctx.message.delete()
    await ctx.author.send("STARTINGING HELP") # Sends a message to the author

    questions = [one] # Create your list of answers

    answers = [] # Empty list as the user will input the answers

    def check(m):
        return ctx.author == m.author and isinstance(m.channel, discord.DMChannel) # Check that the messages were sent in DM by the right author

    for i in questions:
        await ctx.author.send(embed = i) # Sends the questions one after another
        try:
            msg = await pomoci.wait_for('message', timeout=30000, check=check)
        except asyncio.TimeoutError:
            await ctx.author.send("Timeout message.")
            return
               # Sends the questions one after anotherWill no longer proceed, user has to run the command again
        else:
                answers.append(msg)
                 # Sends the questions one after anotherAppends the answers, proceed
    

    
    channel = pomoci.get_channel(999050481622073394)
    lol = discord.Embed(color=ctx.author.color)
    lol.title = f"USER NEEDS HELP "
    user = ctx.message.author.mention
    lol.description = f"**From** : ||{user}||  \n Help: {answers[0].content}"
    await channel.send(embed = lol)
    
    
    
    guild = ctx.guild
    hi = await guild.create_text_channel(name=f"support channel {ctx.author}")
    channel = pomoci.get_channel(hi)
    await hi.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
    
    
    emoji = "✅"
    
    embclose = discord.Embed(title = f"Help ticket",description=f"\n {user} \nSupport will be with you shortly.\nTo close this ticket react with \n {emoji}")
    
    msg = await hi.send(embed = embclose)
    
    
    await msg.add_reaction(emoji )
    
    
    def hii(reaction, user):
      return reaction.message == msg and str(reaction) == "✅"  
    try:
      await pomoci.wait_for("reaction_add", check=hii)  
    except asyncio.TimeoutError:
      ""
    else:
      
      await hi.delete() 

  

    
    
    
    
    
    
    
    
    




    

    
    
  






  




    
    
    
    


pomoci.run(TOKEN)


