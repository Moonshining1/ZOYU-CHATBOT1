import random
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load database connection strings from environment variables
CHAT_STORAGE_URLS = os.getenv("CHAT_STORAGE_URLS")
logger.info(f"CHAT_STORAGE_URLS: {CHAT_STORAGE_URLS}")

if CHAT_STORAGE_URLS:
    CHAT_STORAGE = CHAT_STORAGE_URLS.split(",")
    logger.info(f"CHAT_STORAGE: {CHAT_STORAGE}")
else:
    logger.error("Environment variable CHAT_STORAGE_URLS is not set.")
    raise ValueError("Environment variable CHAT_STORAGE_URLS is not set.")

# Select a random database connection string
def get_random_db_connection():
    try:
        selected_url = random.choice(CHAT_STORAGE)
        logger.info(f"Selected MongoDB connection string: {selected_url}")
        return MongoCli(selected_url)
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        return None

VIPBOY = get_random_db_connection()
if VIPBOY:
    chatdb = VIPBOY.Anonymous
    chatai = chatdb.Word.WordDb
    storeai = VIPBOY.Anonymous.Word.NewWordDb
    logger.info("Database connections established successfully.")
else:
    chatdb = None
    chatai = None
    storeai = None
    logger.error("Failed to establish database connections.")
