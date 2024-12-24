from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER, nexichat

# Constants for callback data
CALLBACK_HELP = "HELP"
CALLBACK_CLOSE = "CLOSE"
CALLBACK_ABOUT = "ABOUT"
CALLBACK_CHATBOT_CMD = "CHATBOT_CMD"
CALLBACK_TOOLS_DATA = "TOOLS_DATA"
CALLBACK_ENABLE_CHATBOT = "enable_chatbot"
CALLBACK_DISABLE_CHATBOT = "disable_chatbot"
CALLBACK_BACK = "BACK"
CALLBACK_SBACK = "SBACK"
CALLBACK_CHATBOT_BACK = "CHATBOT_BACK"
CALLBACK_SOOM = "soom"

START_BOT = [
    [InlineKeyboardButton(text="🛠️ σρεи ¢σммαиdꜱ ⚙️", callback_data=CALLBACK_HELP)],
]

DEV_OP = [
    [InlineKeyboardButton(text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦", url=f"https://t.me/{nexichat.username}?startgroup=true")],
    [InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data=CALLBACK_HELP)],
    [InlineKeyboardButton(text="☁️ ᴀʙᴏᴜᴛ ☁️", callback_data=CALLBACK_ABOUT)],
]

PNG_BTN = [
    [InlineKeyboardButton(text="🛠️ σρεи ¢σммαиdꜱ ⚙️", callback_data=CALLBACK_HELP)],
    [InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data=CALLBACK_CLOSE)],
]

BACK = [
    [InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data=CALLBACK_BACK)],
]

HELP_BTN = [
    [InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data=CALLBACK_CHATBOT_CMD),
     InlineKeyboardButton(text="🎄 ᴛᴏᴏʟs 🎄", callback_data=CALLBACK_TOOLS_DATA)],
    [InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data=CALLBACK_CLOSE)],
]

CLOSE_BTN = [
    [InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data=CALLBACK_CLOSE)],
]

CHATBOT_ON = [
    [InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=CALLBACK_ENABLE_CHATBOT),
     InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=CALLBACK_DISABLE_CHATBOT)],
]

MUSIC_BACK_BTN = [
    [InlineKeyboardButton(text="sᴏᴏɴ", callback_data=CALLBACK_SOOM)],
]

S_BACK = [
    [InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data=CALLBACK_SBACK),
     InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data=CALLBACK_CLOSE)],
]

CHATBOT_BACK = [
    [InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data=CALLBACK_CHATBOT_BACK),
     InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data=CALLBACK_CLOSE)],
]

HELP_START = [
    [InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data=CALLBACK_HELP),
     InlineKeyboardButton(text="🐳 ᴄʟᴏsᴇ 🐳", callback_data=CALLBACK_CLOSE)],
]

HELP_BUTN = [
    [InlineKeyboardButton(text="« ғᴇᴀᴛᴜʀᴇs »", callback_data=CALLBACK_HELP)],
    [InlineKeyboardButton(text="⦿ ᴄʟᴏsᴇ ⦿", callback_data=CALLBACK_CLOSE)],
]

ABOUT_BTN = [
    [InlineKeyboardButton(text="🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
     InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data=CALLBACK_HELP)],
    [InlineKeyboardButton(text="🍾 ᴏᴡɴᴇʀ 🍾", user_id=OWNER)],
    [InlineKeyboardButton(text="🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=f"https://t.me/{UPDATE_CHNL}"),
     InlineKeyboardButton(text="⦿ ʙᴀᴄᴋ ⦿", callback_data=CALLBACK_BACK)],
]
