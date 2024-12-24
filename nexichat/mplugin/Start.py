import asyncio
import logging
import random
import time
import psutil
import config
import os
from nexichat import _boot_, get_readable_time, mongo, CLONE_OWNERS, db
from nexichat.mplugin.helpers import is_owner
from datetime import datetime
from pymongo import MongoClient
from pyrogram.enums import ChatType
from pyrogram import Client, filters
from config import OWNER_ID, MONGO_URL, OWNER_USERNAME
from pyrogram.errors import FloodWait, ChatAdminRequired
from nexichat.database.chats import get_served_chats, add_served_chat
from nexichat.database.users import get_served_users, add_served_user
from nexichat.database.clonestats import get_served_cchats, get_served_cusers, add_served_cuser, add_served_cchat
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from nexichat.mplugin.helpers import (
    START, START_BOT, PNG_BTN, CLOSE_BTN, HELP_BTN, HELP_BUTN, HELP_READ, HELP_START, SOURCE_READ,
)

LOGGER = logging.getLogger(__name__)

OK = "**ʜᴇʏ👀**"
AUTO_MSG = f"""{os.getenv("AUTO_MSG")}""" if os.getenv("AUTO_MSG") else OK
GSTART = """**ʜᴇʏ ᴅᴇᴀʀ {}**\n\n**ᴛʜᴀɴᴋs ғᴏʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ʏᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ɢɪᴠᴇɴ ..."""
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

EMOJIOS = [
    "💣", "💥", "🪄", "🧨", "⚡", "🤡", "👻", "🎃", "🎩", "🕊",
]

BOT = "https://files.catbox.moe/0kpdw9.jpg"
IMG = [
    "https://files.catbox.moe/t57fdb.jpg",
    "https://files.catbox.moe/0ogndc.jpg",
    "https://files.catbox.moe/g41f9e.jpg",
    "https://files.catbox.moe/c9hkff.jpg",
    "https://files.catbox.moe/gudv6v.jpg",
    "https://files.catbox.moe/6xiocz.jpg",
    "https://files.catbox.moe/dz22a1.jpg",
    "https://files.catbox.moe/9iwpfv.jpg",
    "https://files.catbox.moe/3mvh25.jpg",
    "https://files.catbox.moe/nzpm5w.jpg",
    "https://files.catbox.moe/mjez4q.jpg",
    "https://files.catbox.moe/h75qko.jpg",
    "https://files.catbox.moe/68hu5w.jpg",
    "https://files.catbox.moe/rkdx6x.jpg",
]

chatai = db.Word.WordDb
lang_db = db.ChatLangDb.LangCollection
status_db = db.ChatBotStatusDb.StatusCollection
cloneownerdb = db.clone_owners

async def get_clone_owner(bot_id):
    try:
        data = await cloneownerdb.find_one({"bot_id": bot_id})
        return data["user_id"] if data else None
    except Exception as e:
        LOGGER.error(f"Error fetching clone owner: {e}")
        return None

async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    try:
        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent
    except Exception as e:
        LOGGER.error(f"Error fetching system stats: {e}")
        cpu, mem, disk = 0, 0, 0
    return get_readable_time(bot_uptime), f"{cpu}%", f"{mem}%", f"{disk}%"

async def set_default_status(chat_id):
    try:
        if not await status_db.find_one({"chat_id": chat_id}):
            await status_db.insert_one({"chat_id": chat_id, "status": "enabled"})
    except Exception as e:
        LOGGER.error(f"Error setting default status for chat {chat_id}: {e}")

@Client.on_message(filters.new_chat_members)
async def welcomejej(client, message: Message):
    chat = message.chat
    bot_id = client.me.id
    await add_served_cchat(bot_id, chat.id)
    await add_served_chat(chat.id)
    await set_default_status(chat.id)
    users = len(await get_served_cusers(bot_id))
    chats = len(await get_served_cchats(bot_id))
    try:
        for member in message.new_chat_members:
            if member.id == client.me.id:
                try:
                    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("sᴇʟᴇᴄᴛ ʟᴀɴɢᴜᴀɢᴇ", callback_data="choose_lang")]])
                    await message.reply_text(text="**тнαикѕ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴩ.**\n\n**ᴋɪɴᴅʟʏ  ꜱᴇʟᴇᴄᴛ  ʙᴏᴛ  ʟᴀɴɢᴜᴀɢ...**", reply_markup=reply_markup)
                    await message.reply_text(f"**{AUTO_MSG}**")
                except Exception as e:
                    LOGGER.error(f"Error sending welcome message: {e}")
                try:
                    invitelink = await client.export_chat_invite_link(chat.id)
                    link = f"[ɢᴇᴛ ʟɪɴᴋ]({invitelink})"
                except ChatAdminRequired:
                    link = "No Link"
                except Exception as e:
                    LOGGER.error(f"Error exporting chat invite link: {e}")
                    link = "No Link"
                
                try:
                    groups_photo = await client.download_media(chat.photo.big_file_id, file_name=f"chatpp{chat.id}.png")
                    chat_photo = groups_photo if groups_photo else "https://envs.sh/IL_.jpg"
                except AttributeError:
                    chat_photo = "https://envs.sh/IL_.jpg"
                except Exception as e:
                    LOGGER.error(f"Error downloading chat photo: {e}")
                    chat_photo = "https://envs.sh/IL_.jpg"

                count = await client.get_chat_members_count(chat.id)
                username = chat.username if chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                msg = (
                    f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {chat.title}\n"
                    f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** `{chat.id}`\n"
                    f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**🖇️𝐆ʀᴏᴜᴘ 𝐋ɪɴᴋ:** {link}\n"
                    f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                    f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}\n\n"
                    f"**ᴛᴏᴛᴀʟ ᴄʜᴀᴛs :** {chats}"
                )

                try:
                    owner_id = await get_clone_owner(bot_id)
                    if owner_id:
                        await client.send_photo(
                            int(owner_id),
                            photo=chat_photo,
                            caption=msg,
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{message.from_user.first_name}", user_id=message.from_user.id)]])
                        )
                except Exception as e:
                    LOGGER.error(f"Error sending photo to owner: {e}")
    except Exception as e:
        LOGGER.error(f"Error in welcome handler: {e}")

@Client.on_message(filters.command(["start", "aistart"]))
async def start(client: Client, m: Message):
    bot_id = client.me.id
    users = len(await get_served_cusers(bot_id))
    chats = len(await get_served_cchats(bot_id))
    
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(text=random.choice(EMOJIOS))
        animation_steps = [
            "⚡ᴅ", "⚡ᴅι", "⚡ᴅιи", "⚡ᴅιиg", "⚡ᴅιиg ᴅ", "⚡ᴅιиg ᴅσ", "⚡ᴅιиg ᴅσи", "⚡ᴅιиg ᴅσиg", "⚡ᴅιиg ᴅσиg ꨄ︎", "⚡sᴛαятɪиg..."
        ]

        for step in animation_steps:
            await accha.edit(f"**__{step}__**")
            await asyncio.sleep(0.01)

        await accha.delete()
        
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        chat_photo = BOT  
        if m.chat.photo:
            try:
                userss_photo = await client.download_media(m.chat.photo.big_file_id)
                await umm.delete()
                chat_photo = userss_photo if userss_photo else BOT
            except Exception as e:
                LOGGER.error(f"Error downloading user photo: {e}")
                chat_photo = BOT  

        UP, CPU, RAM, DISK = await bot_sys_stats()
        await m.reply_photo(photo=chat_photo, caption=START.format(users, chats, UP), reply_markup=InlineKeyboardMarkup(START_BOT))
        await m.reply_text(f"**{AUTO_MSG}**")
        await add_served_cuser(bot_id, m.chat.id) 
        await add_served_user(m.chat.id)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(f"{m.chat.first_name}", user_id=m.chat.id)]])
        owner_id = await get_clone_owner(bot_id) 
        if owner_id:
            await client.send_photo(
                int(owner_id),
                photo=chat_photo,
                caption=f"{m.from_user.mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ. \n\n**ɴᴀᴍᴇ :** {m.chat.first_name}\n**ᴜsᴇʀɴᴀᴍᴇ :** @{m.chat.username}\n**ɪᴅ :** {m.chat.id}\n",
                reply_markup=keyboard
            )
        
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=GSTART.format(m.from_user.mention or "can't mention"),
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await m.reply_text(f"**{AUTO_MSG}**")
        await add_served_cchat(bot_id, m.chat.id)
        await add_served_chat(m.chat.id)

@Client.on_message(filters.command("help"))
async def help(client: Client, m: Message):
    bot_id = client.me.id
    if m.chat.type == ChatType.PRIVATE:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=HELP_READ,
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption="**ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
            reply_markup=InlineKeyboardMarkup(HELP_BUTN),
        )
        await add_served_cchat(bot_id, m.chat.id)
        await add_served_chat(m.chat.id)

@Client.on_message(filters.command("repo"))
async def repo(client: Client, m: Message):
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )

@Client.on_message(filters.command("ping"))
async def ping(client: Client, message: Message):
    bot_id = client.me.id
    start = datetime.now()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{(await client.get_me()).mention} ᴄʜᴀᴛʙᴏᴛ ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n\n**➥** `{ms}` ms\n**➲ ᴄᴘᴜ:** {CPU}\n**➲ ʀαm:** {RAM}\n**➲ ᴅιѕĸ:** {DISK}",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_cuser(bot_id, message.from_user.id)
        await add_served_user(message.from_user.id)
    else:
        await add_served_cchat(bot_id, message.chat.id)
        await add_served_chat(message.chat.id)

@Client.on_message(filters.command("stats"))
async def stats(cli: Client, message: Message):
    bot_id = (await cli.get_me()).id
    users = len(await get_served_cusers(bot_id))
    chats = len(await get_served_cchats(bot_id))
    
    await message.reply_text(
        f"""{(await cli.get_me()).mention} Chatbot Stats:

➻ **Chats:** {chats}
➻ **Users:** {users}"""
    )

@Client.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"
        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ
