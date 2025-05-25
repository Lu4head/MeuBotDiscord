import discord
import random
from typing import Optional
from discord.ext import commands
from ai.ai_bot import AIBot

intents = discord.Intents.default()
intents.message_content = True

discord_bot = commands.Bot(command_prefix="!",intents=intents)
ai_bot = AIBot()

@discord_bot.event
async def on_ready():
    print(f'We have logged in as {discord_bot.user}')
    print("bot is running...")


@discord_bot.command()
async def roll(ctx, dice: Optional[str]):
    if not dice:
        await ctx.send("Informe sua rolada")
        return

    try:
        numero_de_dados, numero_de_faces = map(int, dice.split('d'))
    except Exception:
        await ctx.send("Formato invalido inserido, não é um numero. Roll deve ester no formato NdN ! ")
        return

    if numero_de_dados < 1 or numero_de_dados > 10000:
        await ctx.send("Número de dados inválido (range valido: 1 -> 10000)")
        return

    if numero_de_faces < 2:
        await ctx.send("Número de faces inválido")
        return

    results = []
    results = [random.randint(1, numero_de_faces)
            for _ in range(numero_de_dados)]
    results_formatado = ', '.join(map(str, results))
    print(type(ctx.author))
    print(ctx.author.mention)
    message = f"""
    :game_die: {ctx.author.mention} Rolada de {dice}
    Resultado: {results_formatado}
    Total: {sum(results)}
    """
    await ctx.send(message)

@discord_bot.command()
async def ia(ctx, *, prompt):
    if not prompt:
        await ctx.send("Desculpe, não entendi sua pergunta.")
    
    await ctx.send(ai_bot.invoke(prompt))
        
    
    
