import config
from telethon import TelegramClient


def start():
    client = TelegramClient('session_name', config.API_ID, config.API_HASH)
    client.start()


start()
