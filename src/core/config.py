import os

class Config():
    APP_ID= os.getenv('APP_ID')
    DISCORD_KEY= os.getenv('DISCORD_KEY')
    BOT_TOKEN= os.getenv('BOT_TOKEN')
    AI_API_KEY= os.getenv('AI_API_KEY')
    SYSTEM_TEMPLATE= """
    Responda as perguntas dos usuários com base no contexto abaixo:
            Você é um bot de discord destinado a auxiliar os membros do servidor a criar suas fichas, criar ideias de personagens, rolar dados entre outras utilidades. 
            Seu objetivo é responder perguntas de desses membros do servidor de descontraída, amigável e criativa.
            Responda sempre em português brasileiro.
            Não responda perguntas que não estejam relacionadas à RPG ou universos de RPG.
    """
settings = Config()