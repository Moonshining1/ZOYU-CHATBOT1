from nexichat import db as mongodb

cloneownerdb = mongodb.cloneownerdb
clonebotdb = mongodb.clonebotdb

def get_bot_users_collection(bot_id):
    return mongodb[f"{bot_id}_users"]

def get_bot_chats_collection(bot_id):
    return mongodb[f"{bot_id}_chats"]

async def is_served_cuser(bot_id, user_id: int) -> bool:
    try:
        usersdb = get_bot_users_collection(bot_id)
        user = await usersdb.find_one({"user_id": user_id})
        return user is not None
    except Exception as e:
        print(f"Error in is_served_cuser: {e}")
        return False

async def add_served_cuser(bot_id, user_id: int):
    try:
        is_served = await is_served_cuser(bot_id, user_id)
        if not is_served:
            usersdb = get_bot_users_collection(bot_id)
            await usersdb.insert_one({"user_id": user_id})
    except Exception as e:
        print(f"Error in add_served_cuser: {e}")

async def get_served_cusers(bot_id) -> list:
    try:
        usersdb = get_bot_users_collection(bot_id)
        return await usersdb.find({"user_id": {"$gt": 0}}).to_list(length=None)
    except Exception as e:
        print(f"Error in get_served_cusers: {e}")
        return []

async def is_served_cchat(bot_id, chat_id: int) -> bool:
    try:
        chatsdb = get_bot_chats_collection(bot_id)
        chat = await chatsdb.find_one({"chat_id": chat_id})
        return chat is not None
    except Exception as e:
        print(f"Error in is_served_cchat: {e}")
        return False

async def add_served_cchat(bot_id, chat_id: int):
    try:
        is_served = await is_served_cchat(bot_id, chat_id)
        if not is_served:
            chatsdb = get_bot_chats_collection(bot_id)
            await chatsdb.insert_one({"chat_id": chat_id})
    except Exception as e:
        print(f"Error in add_served_cchat: {e}")

async def get_served_cchats(bot_id) -> list:
    try:
        chatsdb = get_bot_chats_collection(bot_id)
        return await chatsdb.find({"chat_id": {"$gt": 0}}).to_list(length=None)
    except Exception as e:
        print(f"Error in get_served_cchats: {e}")
        return []
