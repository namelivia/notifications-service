from .base import Base
from telegram.ext import Updater


class Telegram(Base):

    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id

    def send(self, message: str):
        updater = Updater(token=self.token, use_context=True)
        updater.bot.send_message(
            chat_id=self.chat_id,
            text=message
        )
        updater.stop()
