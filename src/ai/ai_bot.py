from google import genai
from google.genai import types
from core.config import settings


class AIBot:
    def __init__(self):
        self.__client = genai.Client(api_key=str(settings.AI_API_KEY))

    def invoke(self, prompt):
        SYSTEM_TEMPLATE = str(f"{settings.SYSTEM_TEMPLATE}")

        response = self.__client.models.generate_content(
            model="gemini-1.5-flash",
            contents= SYSTEM_TEMPLATE + prompt
        )

        return response.text
