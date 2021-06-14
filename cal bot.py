import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def mathadd(ctx, x: float, y: float):
    try:
        result = x + y
        await ctx.send(result)
    except:
        pass

@bot.command()
async def mathsub(ctx, x: float, y: float):
	try:
		result = x - y
		await ctx.send(result)
	except:
		pass

@bot.command()
async def mathdiv(ctx, x: float, y: float):
	try:
		result = x / y
		await ctx.send(result)

	except:
		pass

@bot.command()
async def mathmult(ctx, x: float, y: float):
	try:
		result = x * y
		await ctx.send(result)

	except:
		pass

@bot.command()
async def mathsqrt(ctx, x: float):
	try:
		result = x**2
		await ctx.send(result)

	except:
		pass

@bot.command()
async def command_info(ctx):
    info = ('Visit the readme file at https://github.com/LispyRaiden/Calculator-Bot')
    await ctx.send(info,
    file = discord.File('Thank you.png'))



bot.run(os.getenv("TOKEN"))