import asyncio
import config
import random
from telethon import TelegramClient


# Начинаем работу клиента
async def start_client():

    # Более удобный подход к регистрации своего клиента
    async with TelegramClient('session_name', config.API_ID, config.API_HASH) as client:
        message = ""  # Пустая переменная для фразы

        # Загружаем фразы из текстового файла
        file = open('phrases.txt', encoding="utf8")

        # Заносим все фразы в список
        gachi_phrases = list(set(file))  # Очистка фраз от мусора
        file.close()  # Закроем навсегда текстовый файл

        # Отправляем сообщения нашему челу
        while len(message) < 60:  # Фильтруем мусор по размерам фразы
            message = random.choice(gachi_phrases)  # Выбираем случайную фраза
            await client.send_message(input("Введите имя пользователя: "), message)  # Отправка выбранному пользователю


asyncio.run(start_client())  # Запуск
