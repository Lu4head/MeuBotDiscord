from bot.discord_bot import discord_bot
from core.config import settings

discord_bot.run(settings.BOT_TOKEN)