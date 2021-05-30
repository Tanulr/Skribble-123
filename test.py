import discord
import random
from discord.ext import commands, tasks

# creating a bot
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def skribble123(ctx):
    # Accesses member object (in this case the author of the message) and sends them a DM while mentioning them
    await ctx.send(f'Hello {ctx.author.mention}!')

@client.command()
async def instructions(ctx):
    # Accesses member object (in this case the author of the message) and sends them a DM while mentioning them
    await ctx.send(f"1. Type .play to get a new drawing.\n2. Type in your guess in the format .guess <ans>\n3. If the answer is right you are credited with points based on difficulty of the word. \n4. To know final tally of points type .tally.\n")

files = [['eyelash.jpg', "eyelash", 10], ['harrypotter.jpg', "harry potter", 10], ['head.jpg', "head", 5], ['hospital.jpg', "hospital", 5], ['lava.jpg', "lava", 10], ['nike.jpg', "nike", 5], ['radio.jpg', "radio", 5], ['rockstar.jpg', "rockstar", 5]]
index = random.randint(0,7)

@client.command()
async def play(ctx):
    # Accesses member object (in this case the author of the message) and sends them a DM while mentioning them
    
    await ctx.send(file=discord.File(f'{files[index][0]}'))

sum = 0

@client.command()
async def guess(ctx, *, ans):
    global sum
    if ans == files[index][1].lower():
        await ctx.send(f"Right answer! You get {files[index][2]} points.")
        sum += files[index][2]
    else:
        await ctx.send(f"Whoops! Wrong answer.")

@client.command(aliases=['tally'])
async def test_tally(ctx):
    embed = discord.Embed(title="Skribble on Discord", color=discord.Color.green())
    embed.add_field(name="Tally", value=f"{sum}", inline=False)
    embed.add_field(name="Player", value=f"{ctx.author.mention}", inline=False)
    #https://cog-creators.github.io/discord-embed-sandbox/
    await ctx.send(embed=embed)

# running the bot
client.run("ODQ4NTQyNDY5MDQ1NDg1NTY4.YLOIwQ.WtSwH07xc7bEkMcQcukkkQ41dg8")