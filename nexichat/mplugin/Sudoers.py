from pyrogram import filters, Client
from pyrogram.types import Message
from config import MONGO_URL, OWNER_ID
from nexichat import nexichat as app
from nexichat import SUDOERS
from nexichat.database import add_sudo, remove_sudo
import logging

LOGGER = logging.getLogger(__name__)

@Client.on_message(filters.command("addsudo") & filters.user(OWNER_ID))
async def useradd(client, message: Message):
    if MONGO_URL is None:
        return await message.reply_text(
            "**Due to bot's privacy issues, you can't manage sudo users when you're using Yukki's database. Please fill your MONGO_DB_URI in your vars to use this feature.**"
        )
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("Reply to a user's message or provide username/user_id.")
    
    user = message.reply_to_message.from_user if message.reply_to_message else None
    if not user:
        user_identifier = message.text.split(None, 1)[1]
        if "@" in user_identifier:
            user_identifier = user_identifier.replace("@", "")
        user = await client.get_users(user_identifier)
    
    if user.id in SUDOERS:
        return await message.reply_text(f"{user.mention} is already a sudo user.")
    
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(f"Added **{user.mention}** to sudo users.")
    else:
        LOGGER.error(f"Failed to add {user.id} to sudo users.")
        await message.reply_text("Failed to add user to sudo users.")

@Client.on_message(filters.command(["rmsudo", "delsudo"]) & filters.user(OWNER_ID))
async def userdel(client, message: Message):
    if MONGO_URL is None:
        return await message.reply_text(
            "**Due to bot's privacy issues, you can't manage sudo users when you're using Yukki's database. Please fill your MONGO_DB_URI in your vars to use this feature.**"
        )
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("Reply to a user's message or provide username/user_id.")
    
    user = message.reply_to_message.from_user if message.reply_to_message else None
    if not user:
        user_identifier = message.text.split(None, 1)[1]
        if "@" in user_identifier:
            user_identifier = user_identifier.replace("@", "")
        user = await client.get_users(user_identifier)
    
    if user.id not in SUDOERS:
        return await message.reply_text("Not a part of bot's sudo.")
    
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text("Removed from bot's sudo users.")
    else:
        LOGGER.error(f"Failed to remove {user.id} from sudo users.")
        await message.reply_text("Something went wrong.")

@Client.on_message(filters.command(["sudo", "sudolist"]))
async def sudoers_list(client, message: Message):
    text = "🔥<u> **Owner:**</u>\n"
    count = 0
    try:
        user = await client.get_users(OWNER_ID)
        user_name = user.first_name if not user.mention else user.mention
        count += 1
        text += f"{count}➤ {user_name}\n"
    except Exception as e:
        LOGGER.error(f"Failed to fetch owner info: {e}")
    
    smex = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await client.get_users(user_id)
                user_name = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n🔥<u> **Sudoers:**</u>\n"
                count += 1
                text += f"{count}➤ {user_name} ({user.id})\n"
            except Exception as e:
                LOGGER.error(f"Failed to fetch sudo user info: {e}")

    if count == 0:
        await message.reply_text("No sudo users found.")
    else:
        await message.reply_text(text)
