import os
import discord
import random
from typing import Optional
from discord.ext import commands
from google import genai

ai_client = genai.Client(api_key=os.getenv("AI_API_KEY"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print("bot is running...")
        
@bot.command()
async def teste(ctx, arg: Optional[str] = ''):
    await ctx.send(f"Hello {arg}!")

@bot.command()
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
    results = [random.randint(1, numero_de_faces) for _ in range(numero_de_dados)]
    results_formatado = ', '.join(map(str, results))
    message = f"""
    :game_die: Rolada de {dice}
    Resultado: {results_formatado}
    Total: {sum(results)}
    """
    await ctx.send(message)

@bot.command()
async def ai(ctx, *, prompt):
    response = ai_client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
    await ctx.send(response.text)
        
bot.run(os.getenv("BOT_TOKEN"))

    