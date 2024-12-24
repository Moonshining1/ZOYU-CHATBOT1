import random
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
import os

# Load database connection strings from environment variables
CHAT_STORAGE = os.getenv("CHAT_STORAGE_URLS").split("mongodb+srv://chatbot1:a@cluster0.pxbu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot2:b@cluster0.9i8as.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot3:c@cluster0.0ak9k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot4:d@cluster0.4i428.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot5:e@cluster0.pmaap.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot6:f@cluster0.u63li.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot7:g@cluster0.mhzef.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot8:h@cluster0.okxao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot9:i@cluster0.yausb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://chatbot10:j@cluster0.9esnn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",)

# Select a random database connection string
def get_random_db_connection():
    try:
        return MongoCli(random.choice(CHAT_STORAGE))
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

VIPBOY = get_random_db_connection()
if VIPBOY:
    chatdb = VIPBOY.Anonymous
    chatai = chatdb.Word.WordDb
    storeai = VIPBOY.Anonymous.Word.NewWordDb
else:
    chatdb = None
    chatai = None
    storeai = None
