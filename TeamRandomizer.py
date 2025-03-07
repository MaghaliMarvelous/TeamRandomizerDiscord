import discord
from discord.ext import commands
import random
import pandas as pd

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def randomize_teams(players, team_size):
    random.shuffle(players)
    teams = [players[i:i + team_size] for i in range(0, len(players), team_size)]
    return teams

def format_teams_table(teams):
    team_data = {"Team": [], "Players": []}
    for i, team in enumerate(teams, 1):
        team_data["Team"].append(f"Team {i}")
        team_data["Players"].append(", ".join(team))

    df = pd.DataFrame(team_data)
    return f"```{df.to_string(index=False)}```"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def team(ctx, team_size: int, *players):
    if len(players) < 2:
        await ctx.send("Please provide at least two players.")
        return

    teams = randomize_teams(list(players), team_size)
    result_table = format_teams_table(teams)
    
    await ctx.send(f"🎲 **Randomized Teams:**\n{result_table}")

bot.run("YOUR_BOT_TOKEN")
