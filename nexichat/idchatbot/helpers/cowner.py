from nexichat import db, SUDOERS
from config import OWNER_ID

cloneownerdb = db.clone_owners

async def save_idclonebot_owner(clone_id, user_id):
    """
    Save the owner of the clone bot.
    Parameters:
    - clone_id: ID of the clone bot.
    - user_id: ID of the user.
    """
    await cloneownerdb.update_one(
        {"clone_id": clone_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def get_idclone_owner(clone_id):
    """
    Retrieve the owner of the clone bot.
    Parameters:
    - clone_id: ID of the clone bot.
    Returns:
    - user_id: ID of the user if found, else None.
    """
    data = await cloneownerdb.find_one({"clone_id": clone_id})
    return data["user_id"] if data else None

async def is_owner(clone_id, user_id):
    """
    Check if the user is the owner of the clone bot.
    Parameters:
    - clone_id: ID of the clone bot.
    - user_id: ID of the user.
    Returns:
    - True if the user is the owner, else False.
    """
    owner_id = await get_idclone_owner(clone_id)
    return owner_id == user_id or user_id == OWNER_ID or user_id in SUDOERS
