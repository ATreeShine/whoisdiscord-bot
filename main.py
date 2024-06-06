import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='whois!', intents=intents)
# You can use any prefix over here ^
@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')

@bot.command()
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(title=f"Who is {member}", description=member.mention, color=0x00ff00)
    embed.set_thumbnail(url=member.avatar_url)
    
    embed.add_field(name="Name", value=str(member), inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Joined Discord on", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Joined Server on", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Pronouns", value=member.display_name, inline=True)  # This can be changed as needed
    embed.add_field(name="About Me", value=member.activity, inline=True)  # This can be changed as needed
    
    # If you have linked accounts setup via Discord Connections, this is a place-holder for demonstration.
    connections = "No connected accounts"
    embed.add_field(name="Connected Accounts", value=connections, inline=True)
    
    await ctx.send(embed=embed)

bot.run('paste yout bot token here')
