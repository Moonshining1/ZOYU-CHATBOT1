from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from nexichat import nexichat as app
from config import UPDATE_CHNL as MUST_JOIN

@app.on_message(filters.incoming, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        await app.get_chat_member(MUST_JOIN, msg.from_user.id)
    except UserNotParticipant:
        if MUST_JOIN.isalpha():
            link = "https://t.me/" + MUST_JOIN
        else:
            chat_info = await app.get_chat(MUST_JOIN)
            link = chat_info.invite_link

        try:
            await msg.reply_photo(
                photo="https://files.catbox.moe/vwzw0q.jpg",
                caption=(f"**👋 Hey {msg.from_user.mention},**\n\n"
                         f"**Join our [Channel](https://t.me/shayariAlfaazonKaAaina) to start messaging here. It's quick and easy!**"),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("๏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ๏", url=link)]])
            )
            await msg.stop_propagation()
        except ChatWriteForbidden:
            print("Cannot write to chat. Please check bot permissions.")
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
