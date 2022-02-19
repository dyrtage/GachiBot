import asyncio
import config
import random
from telethon import TelegramClient


# Начинаем работу клиента
async def start_client():
    async with TelegramClient('session_name', config.API_ID, config.API_HASH) as client:
        # Загружаем фразы из текстового файла
        file = open('phrases.txt', encoding="utf8")
        message = ""

        # Заносим все фразы в список
        gachi_phrases = list(set(file))  # Очистка фраз от мусора
        file.close()

        # Отправляем сообщения нашему челу
        while len(message) < 40:
            message = random.choice(gachi_phrases)  # Случайная фраза
            await client.send_message('C_h_e_l_l', message)  # Отправка выбранному пользователю


asyncio.run(start_client())
