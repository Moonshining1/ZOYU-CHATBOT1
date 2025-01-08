import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
import config
import logging

# Configure logging
logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
LOGGER = logging.getLogger(__name__)

class Userbot(Client):
    def __init__(self):
        super().__init__(
            name="VIPAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=config.STRING1,
            no_updates=False,
            plugins=dict(root="nexichat.idchatbot"),
        )

    async def start(self):
        LOGGER.info("Starting Id chatbot...")
        if config.STRING1:
            await self.start_client()

    async def start_client(self):
        try:
            await self.start()
            await self.join_required_chats()
            self.set_client_attributes()
            LOGGER.info(f"Id-Chatbot Started as {self.me.first_name}")
        except Exception as e:
            LOGGER.error(f"Failed to start Id-Chatbot: {e}")

    async def join_required_chats(self):
        try:
            await self.join_chat("shayariAlfaazonKaAaina")
            await self.join_chat("grandxmasti")
        except Exception as e:
            LOGGER.warning(f"Failed to join required chats: {e}")

    def set_client_attributes(self):
        self.id = self.me.id
        self.name = self.me.mention
        self.username = self.me.username

    async def stop(self):
        LOGGER.info("Stopping Id-Chatbot...")
        try:
            if config.STRING1:
                await self.stop_client()
        except Exception as e:
            LOGGER.error(f"Failed to stop Id-Chatbot: {e}")

    async def stop_client(self):
        await self.stop()
