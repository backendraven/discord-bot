import os
import random

import discord
from discord.ext import commands

# Токен берём из переменной окружения, чтобы не хранить его в коде
TOKEN = os.getenv("DISCORD_TOKEN")

# Для чтения текста сообщений нужен интент message_content
intents = discord.Intents.default()
intents.message_content = True

# help_command=None — отключаем встроенную !help, у нас своя !помощь
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Бот {bot.user} готов к работе!")


@bot.command(name="привет")
async def privet(ctx):
    await ctx.send(f"Привет, {ctx.author.mention}!")


@bot.command(name="кубик")
async def kubik(ctx):
    await ctx.send(f"🎲 Выпало: {random.randint(1, 6)}")


@bot.command(name="монетка")
async def monetka(ctx):
    await ctx.send(f"🪙 {random.choice(['орёл', 'решка'])}")


@bot.command(name="помощь")
async def pomosh(ctx):
    await ctx.send(
        "**Что я умею:**\n"
        "`!привет` — поздороваюсь с тобой\n"
        "`!кубик` — брошу кубик (1–6)\n"
        "`!монетка` — подброшу монетку (орёл или решка)\n"
        "`!помощь` — покажу этот список"
    )


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Такой команды нет, напиши `!помощь`")
    else:
        raise error


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Не найден токен: задай переменную окружения DISCORD_TOKEN")
    bot.run(TOKEN)