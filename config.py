from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Required configurations
API_ID = getenv("API_ID", "6435225")
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")

# Optional configurations with default values
BOT_TOKEN = getenv("BOT_TOKEN")
STRING1 = getenv("STRING_SESSION")
MONGO_URL = getenv("MONGO_URL")

# Convert OWNER_ID to int and handle errors
try:
    OWNER_ID = int(getenv("OWNER_ID", "7745014754"))
except ValueError:
    raise ValueError("OWNER_ID must be an integer")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/villian26/VILLIAN-CHATBOT")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# Support group and update channel
SUPPORT_GRP = getenv("SUPPORT_GRP", "ll_KINGDOM_ll")
UPDATE_CHNL = getenv("UPDATE_CHNL", "ll_IMPERIAL_ll")

# Owner's username and optional git token for private repositories
OWNER_USERNAME = getenv("OWNER_USERNAME", "IT_AMRIT")
GIT_TOKEN = getenv("GIT_TOKEN", "")

# For debugging purposes, you can print the loaded configuration
if __name__ == "__main__":
    print(f"API_ID: {API_ID}")
    print(f"API_HASH: {API_HASH}")
    print(f"BOT_TOKEN: {BOT_TOKEN}")
    print(f"STRING1: {STRING1}")
    print(f"MONGO_URL: {MONGO_URL}")
    print(f"OWNER_ID: {OWNER_ID}")
    print(f"UPSTREAM_REPO: {UPSTREAM_REPO}")
    print(f"UPSTREAM_BRANCH: {UPSTREAM_BRANCH}")
    print(f"SUPPORT_GRP: {SUPPORT_GRP}")
    print(f"UPDATE_CHNL: {UPDATE_CHNL}")
    print(f"OWNER_USERNAME: {OWNER_USERNAME}")
    print(f"GIT_TOKEN: {GIT_TOKEN}")
