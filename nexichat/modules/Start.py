import asyncio
import os
import logging
import random
import time
import psutil
import config
from nexichat import _boot_, get_readable_time, nexichat, mongo, SUDOERS
from datetime import datetime
from pymongo import MongoClient
from pyrogram.enums import ChatType
from pyrogram import Client, filters
from config import OWNER_ID, MONGO_URL, OWNER_USERNAME
from pyrogram.errors import FloodWait, ChatAdminRequired
from nexichat.database.chats import get_served_chats, add_served_chat
from nexichat.database.users import get_served_users, add_served_user
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from nexichat.modules.helpers import (
    START,
    START_BOT,
    PNG_BTN,
    CLOSE_BTN,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
)
OK = "**ʜᴇʏ👀**"
AUTO_MSG = f"""{os.getenv("AUTO_MSG")}""" if os.getenv("AUTO_MSG") else OK
GSTART = """**ʜᴇʏ ᴅᴇᴀʀ {}**\n\n**ᴛʜᴀɴᴋs ғᴏʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ʏᴏᴜ ᴄᴀɴ ᴄʜᴀɴɢᴇ ʟᴀɴɢᴜᴀɢᴇ ʙʏ ᴄʟɪᴄᴋ ᴏɴ ɢɪᴠᴇɴ �[...]
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]

BOT = "https://files.catbox.moe/rkdx6x.jpg"
IMG = [
    "https://files.catbox.moe/68hu5w.jpg",
    "https://files.catbox.moe/h75qko.jpg",
    "https://files.catbox.moe/mjez4q.jpg",
    "https://files.catbox.moe/nzpm5w.jpg",
    "https://files.catbox.moe/3mvh25.jpg",
    "https://files.catbox.moe/9iwpfv.jpg",
    "https://files.catbox.moe/dz22a1.jpg",
    "https://files.catbox.moe/0kpdw9.jpg",
    "https://files.catbox.moe/6xiocz.jpg",
    "https://files.catbox.moe/gudv6v.jpg",
    "https://files.catbox.moe/c9hkff.jpg",
    "https://files.catbox.moe/g41f9e.jpg",
    "https://files.catbox.moe/t57fdb.jpg",
    "https://files.catbox.moe/0ogndc.jpg",
]


from nexichat import db

chatai = db.Word.WordDb
lang_db = db.ChatLangDb.LangCollection
status_db = db.ChatBotStatusDb.StatusCollection

async def bot_sys_stats():
    """Fetch system statistics for the bot."""
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time((bot_uptime))}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK

async def set_default_status(chat_id):
    """Set the default status for a chat."""
    try:
        if not await status_db.find_one({"chat_id": chat_id}):
            await status_db.insert_one({"chat_id": chat_id, "status": "enabled"})
    except Exception as e:
        print(f"Error setting default status for chat {chat_id}: {e}")

@nexichat.on_message(filters.new_chat_members)
async def welcomejej(client, message: Message):
    """Welcome new chat members."""
    chat = message.chat
    await add_served_chat(message.chat.id)
    await set_default_status(message.chat.id)
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    try:
        for member in message.new_chat_members:
            if member.id == nexichat.id:
                try:
                    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("sᴇʟᴇᴄᴛ ʟᴀɴɢᴜᴀɢᴇ", callback_data="choose_lang")]])    
                    await message.reply_text("**тнαикѕ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ ᴛнɪs ɢʀᴏᴜᴘ.**\n\n**ᴋɪɴᴅʟʏ  ꜱᴇʟᴇᴄᴛ  ʙᴏᴛ  ʟᴀɴɢᴜᴀɢ��[...]
                    await message.reply_text(f"**{AUTO_MSG}**")
                except Exception as e:
                    print(f"{e}")
                    pass
                try:
                    invitelink = await nexichat.export_chat_invite_link(message.chat.id)
                    link = f"[ɢᴇᴛ ʟɪɴᴋ]({invitelink})"
                except ChatAdminRequired:
                    link = "No Link"

                try:
                    groups_photo = await nexichat.download_media(
                        chat.photo.big_file_id, file_name=f"chatpp{chat.id}.png"
                    )
                    chat_photo = (
                        groups_photo if groups_photo else "https://files.catbox.moe/4xigtl.jpg"
                    )
                except AttributeError:
                    chat_photo = "https://files.catbox.moe/nphfkc.jpg"
                except Exception as e:
                    pass

                count = await nexichat.get_chat_members_count(chat.id)
                chats = len(await get_served_chats())
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
                    OWNER = config.OWNER_ID
                    if OWNER:
                        await nexichat.send_photo(
                            int(OWNER_ID),
                            photo=chat_photo,
                            caption=msg,
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{message.from_user.first_name}", user_id=message.from_user.id)]]))
                except Exception as e:
                    print(f"Please Provide me correct owner id for send logs")
                    await nexichat.send_photo(
                        int(OWNER_ID),
                        photo=chat_photo,
                        caption=msg,
                        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{message.from_user.first_name}", user_id=message.from_user.id)]]))
    except Exception as e:
        print(f"Err: {e}")

from pathlib import Path
import os
import time
import io

@nexichat.on_message(
    filters.command(["ls"]) & filters.user(int(OWNER_ID))
)
async def ls(_, m: Message):
    """List all files and folders."""
    cat = "".join(m.text.split(maxsplit=1)[1:])
    path = cat or os.getcwd()
    if not os.path.exists(path):
        await m.reply_text(
            f"There is no such directory or file with the name `{cat}`. Check again."
        )
        return

    path = Path(cat) if cat else os.getcwd()
    if os.path.isdir(path):
        if cat:
            msg = f"Folders and Files in `{path}`:\n"
        else:
            msg = "Folders and Files in Current Directory:\n"
        lists = os.listdir(path)
        files = ""
        folders = ""
        for contents in sorted(lists):
            catpath = os.path.join(path, contents)
            if not os.path.isdir(catpath):
                size = os.stat(catpath).st_size
                if str(contents).endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += f"🎵`{contents}`\n"
                elif str(contents).endswith((".opus")):
                    files += f"🎙`{contents}`\n"
                elif str(contents).endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
                    files += f"🎞`{contents}`\n"
                elif str(contents).endswith((".zip", ".tar", ".tar.gz", ".rar")):
                    files += f"🗜`{contents}`\n"
                elif str(contents).endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")):
                    files += f"🖼`{contents}`\n"
                else:
                    files += f"📄`{contents}`\n"
            else:
                folders += f"📁`{contents}`\n"
        msg = msg + folders + files if files or folders else f"{msg}__empty path__"
    else:
        size = os.stat(path).st_size
        msg = "The details of the given file:\n"
        if str(path).endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎵"
        elif str(path).endswith((".opus")):
            mode = "🎙"
        elif str(path).endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
            mode = "🎞"
        elif str(path).endswith((".zip", ".tar", ".tar.gz", ".rar")):
            mode = "🗜"
        elif str(path).endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")):
            mode = "🖼"
        else:
            mode = "📄"
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        msg += f"**Location:** `{path}`\n"
        msg += f"**Icon:** `{mode}`\n"
        msg += f"**Size:** `{humanbytes(size)}`\n"
        msg += f"**Last Modified Time:** `{time2}`\n"
        msg += f"**Last Accessed Time:** `{time3}`"

    if len(msg) > 4096:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "ls.txt"
            await m.reply_document(
                out_file,
                caption=path,
            )
    else:
        await m.reply_text(msg)

@nexichat.on_cmd(["start", "aistart"])
async def start(_, m: Message):
    """Handle the start command."""
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(text=random.choice(EMOJIOS))
        await asyncio.sleep(0.5)
        
        await accha.edit("**__ꨄ︎ ѕ__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ sт__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ︎ ѕтα__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ︎ ѕтαя__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ sтαят__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ︎ sтαятι__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ︎ sтαятιи__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ sтαятιиg__**")
        await asyncio.sleep(0.01)
        await accha.edit("**__ꨄ︎ ѕтαятιиg.__**")
        await asyncio.sleep(0.1)
        await accha.edit("**__ꨄ sтαятιиg.....__**")
        await asyncio.sleep(0.1)
        await accha.edit("**__ꨄ︎ ѕтαятιиg.__**")
        await asyncio.sleep(0.1)
        await accha.edit("**__ꨄ sтαятιиg.....__**")
        await accha.delete()
        
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        chat_photo = BOT  
        if m.chat.photo:
            try:
                userss_photo = await nexichat.download_media(m.chat.photo.big_file_id)
                await umm.delete()
                if userss_photo:
                    chat_photo = userss_photo
            except AttributeError:
                chat_photo = BOT  

        users = len(await get_served_users())
        chats = len(await get_served_chats())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await m.reply_photo(photo=chat_photo, caption=START.format(nexichat.mention or "can't mention", users, chats, UP), reply_markup=InlineKeyboardMarkup(START_BOT))
        await m.reply_text(f"**{AUTO_MSG}**")
        await add_served_user(m.chat.id)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(f"{m.chat.first_name}", user_id=m.chat.id)]])
        await nexichat.send_photo(int(OWNER_ID), photo=chat_photo, caption=f"{m.from_user.mention} ʜᴀs sᴛᴀʀᴛᴇᴅ ʙᴏᴛ. \n\n**ɴᴀᴍᴇ :** {m.chat.first_name}\n**ᴜsᴇʀɴᴀᴍᴇ[...]
        
    else:
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=GSTART.format(m.from_user.mention or "can't mention"),
            reply_markup=InlineKeyboardMarkup(HELP_START),
        )
        await m.reply_text(f"**{AUTO_MSG}**")
        await add_served_chat(m.chat.id)

@nexichat.on_cmd("help")
async def help(client: nexichat, m: Message):
    """Handle the help command."""
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
        await add_served_chat(m.chat.id)

@nexichat.on_cmd("repo")
async def repo(_, m: Message):
    """Handle the repo command."""
    await m.reply_text(
        text=SOURCE_READ,
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )

@nexichat.on_cmd("ping")
async def ping(_, message: Message):
    """Handle the ping command."""
    start = datetime.now()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{nexichat.name}
