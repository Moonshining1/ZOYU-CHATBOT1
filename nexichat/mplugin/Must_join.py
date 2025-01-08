
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from nexichat import nexichat
from config import UPDATE_CHNL as MUST_JOIN

@Client.on_message(filters.incoming, group=-2)
async def must_join_channel(client: Client, msg: Message):
    user_id = msg.from_user.id
    if not MUST_JOIN:
        return
    try:
        await nexichat.get_chat_member(MUST_JOIN, user_id)
    except UserNotParticipant:
        if MUST_JOIN.isalpha():
            link = f"https://t.me/{MUST_JOIN}"
        else:
            chat_info = await nexichat.get_chat(MUST_JOIN)
            link = chat_info.invite_link
        try:
            await msg.reply_photo(
                photo="https://files.catbox.moe/vwzw0q.jpg,
                caption=(f"**👋 ʜᴇʟʟᴏ {msg.from_user.mention},**\n\n"
                         f"**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ [ᴄʜᴀɴɴᴇʟ](https://t.me/shayariAlfaazonKaAaina) ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇs ʜᴇʀᴇ.**"),
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("๏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ๏", url=link)]])
            )
            await msg.stop_propagation()
        except ChatWriteForbidden:
            pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")

