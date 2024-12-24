import random
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load database connection strings from environment variables
CHAT_STORAGE_URLS = os.getenv("mongodb+srv://chatbot1:a@cluster0.pxbu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot2:b@cluster0.9i8as.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot3:c@cluster0.0ak9k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot4:d@cluster0.4i428.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot5:e@cluster0.pmaap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot6:f@cluster0.u63li.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot7:g@cluster0.mhzef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot8:h@cluster0.okxao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot9:i@cluster0.yausb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot10:j@cluster0.9esnn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"")
logger.info(f"CHAT_STORAGE_URLS: {CHAT_STORAGE_URLS}")

if CHAT_STORAGE_URLS:
    # Split the connection strings by commas and remove any extra whitespace
    CHAT_STORAGE = [url.strip() for url in CHAT_STORAGE_URLS.split("mongodb+srv://chatbot1:a@cluster0.pxbu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot2:b@cluster0.9i8as.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot3:c@cluster0.0ak9k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot4:d@cluster0.4i428.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot5:e@cluster0.pmaap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot6:f@cluster0.u63li.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot7:g@cluster0.mhzef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot8:h@cluster0.okxao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot9:i@cluster0.yausb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0,mongodb+srv://chatbot10:j@cluster0.9esnn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")]
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
    try:
        chatdb = VIPBOY.Anonymous
        chatai = chatdb.Word.WordDb
        storeai = VIPBOY.Anonymous.Word.NewWordDb
        logger.info("Database connections established successfully.")
    except Exception as e:
        logger.error(f"Error initializing database collections: {e}")
        chatdb = None
        chatai = None
        storeai = None
else:
    chatdb = None
    chatai = None
    storeai = None
    logger.error("Failed to establish database connections.")
