from nexichat import db

chatsdb = db.chatsdb

async def get_served_chats() -> list:
    try:
        chats = chatsdb.find({"chat_id": {"$lt": 0}})
        return await chats.to_list(length=None)
    except Exception as e:
        print(f"Error in get_served_chats: {e}")
        return []

async def is_served_chat(chat_id: int) -> bool:
    try:
        chat = await chatsdb.find_one({"chat_id": chat_id})
        return chat is not None
    except Exception as e:
        print(f"Error in is_served_chat: {e}")
        return False

async def add_served_chat(chat_id: int):
    try:
        if not await is_served_chat(chat_id):
            await chatsdb.insert_one({"chat_id": chat_id})
    except Exception as e:
        print(f"Error in add_served_chat: {e}")

async def remove_served_chat(chat_id: int):
    try:
        if await is_served_chat(chat_id):
            await chatsdb.delete_one({"chat_id": chat_id})
    except Exception as e:
        print(f"Error in remove_served_chat: {e}")
