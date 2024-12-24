import random
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from nexichat import nexichat
from nexichat.database import get_served_chats

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")

SHAYRI = [
    " 🌺**बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।**🌺 \n\n**🥀Bahut aacha lagta hai ...",
    " 🌺**मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।**🌺 \n\n**🥀Meri zindagi Meri ...",
    " 🌺**तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।**🌺 \n\n**🥀**Tum Meri Wo ...",
    # Additional shayari lines...
]

night_shayari = ["🌙 ɢᴏᴏᴅ ɴɪɢʜᴛ! ᴍᴀʏ ʏᴏᴜʀ ᴅʀᴇᴀᴍꜱ ʙᴇ ᴀꜱ ꜱᴡᴇᴇᴛ ᴀꜱ ᴛʜᴇ ꜰɪʀꜱᴛ ʙɪᴛᴇ ᴏꜰ ʏᴏᴜʀ ꜰᴀᴠᴏʀɪᴛᴇ ..."]
morning_shayari = ["🌅 ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ! ᴍᴀʏ ʏᴏᴜʀ ᴅᴀʏ ʙᴇ ᴀꜱ ʙʀɪɢʜᴛ ᴀɴᴅ ᴄʜᴇᴇʀꜰᴜʟ ᴀꜱ ᴛʜᴇ ʀɪꜱɪɴɢ ꜱᴜɴ. ..."]

SHAYRI_COMMAND = ["gf", "bf", "shayri", "sari", "shari", "love"]

@nexichat.on_message(filters.command(SHAYRI_COMMAND))
async def shayri(client: Client, message: Message):
    try:
        await message.reply_text(
            text=random.choice(SHAYRI),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✨𝚂𝚄𝙿𝙿𝙾𝚁𝚃✨", url=f"https://t.me/ll_KINGDOM_ll"),
                     InlineKeyboardButton("✨𝙾𝙵𝙵𝙸𝙲𝙴✨", url=f"https://t.me/ll_IMPERIAL_ll")]
                ]
            ),
        )
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

add_buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="๏ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ๏", url=f"https://t.me/{nexichat.username}?startgroup=true")]
    ]
)

async def send_good_night():
    try:
        schats = await get_served_chats()
        chats = [int(chat["chat_id"]) for chat in schats]
        if not chats:
            return
        for chat_id in chats:
            try:
                shayari = random.choice(night_shayari)
                await nexichat.send_photo(
                    chat_id,
                    photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
                    caption=f"**{shayari}**",
                    reply_markup=add_buttons,
                )
            except Exception as e:
                print(f"Error sending good night message to chat {chat_id}: {e}")
    except Exception as e:
        print(f"Error fetching served chats: {e}")

async def send_good_morning():
    try:
        schats = await get_served_chats()
        chats = [int(chat["chat_id"]) for chat in schats]
        if not chats:
            return
        for chat_id in chats:
            try:
                shayari = random.choice(morning_shayari)
                await nexichat.send_photo(
                    chat_id,
                    photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                    caption=f"**{shayari}**",
                    reply_markup=add_buttons,
                )
            except Exception as e:
                print(f"Error sending good morning message to chat {chat_id}: {e}")
    except Exception as e:
        print(f"Error fetching served chats: {e}")

async def restart_nexichat():
    os.system(f"kill -9 {os.getpid()} && bash start")

scheduler.add_job(send_good_night, trigger="cron", hour=23, minute=50)
scheduler.add_job(send_good_morning, trigger="cron", hour=6, minute=0)
scheduler.add_job(restart_nexichat, trigger="cron", hour=0, minute=0)
scheduler.add_job(restart_nexichat, trigger="cron", hour=7, minute=0)
scheduler.add_job(restart_nexichat, trigger="cron", hour=12, minute=0)
scheduler.add_job(restart_nexichat, trigger="cron", hour=15, minute=0)
scheduler.add_job(restart_nexichat, trigger="cron", hour=18, minute=0)
scheduler.add_job(restart_nexichat, trigger="cron", hour=21, minute=0)
scheduler.start()
