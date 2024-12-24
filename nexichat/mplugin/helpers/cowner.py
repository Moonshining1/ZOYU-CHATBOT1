from nexichat import db, SUDOERS
from config import OWNER_ID

# Database collection for clone owners
cloneownerdb = db.clone_owners

# Function to retrieve the owner of a clone by bot ID
async def get_clone_owner(bot_id):
    try:
        data = await cloneownerdb.find_one({"bot_id": bot_id})
        if data:
            return data["user_id"]
    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error retrieving clone owner: {e}")
    return None

# Function to check if a user is an owner of a bot
async def is_owner(bot_id, user_id):
    try:
        owner_id = await get_clone_owner(bot_id)
        if owner_id == user_id or user_id == OWNER_ID or user_id in SUDOERS:
            return True
    except Exception as e:
        # Log the error or handle it as needed
        print(f"Error checking owner status: {e}")
    return False
