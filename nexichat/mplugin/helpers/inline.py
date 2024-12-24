from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER, nexichat

# InlineKeyboardButton groups for different functionalities

START_BOT = [
    [
        InlineKeyboardButton(text="🛠️ Open Commands ⚙️", callback_data="HELP"),
    ],
]

DEV_OP = [
    [
        InlineKeyboardButton(
            text="✦ Add Me Baby ✦",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« Help »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="☁️ About ☁️", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(text="🛠️ Open Commands ⚙️", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(
            text="⦿ Close ⦿",
            callback_data="CLOSE",
        ),
    ],
]

BACK = [
    [
        InlineKeyboardButton(text="⦿ Back ⦿", callback_data="BACK"),
    ],
]

HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 Chatbot 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 Tools 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⦿ Close ⦿", callback_data="CLOSE"),
    ],
]

CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⦿ Close ⦿", callback_data="CLOSE"),
    ],
]

CHATBOT_ON = [
    [
        InlineKeyboardButton(text="Enable", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="Disable", callback_data="disable_chatbot"),
    ],
]

MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="Soon", callback_data="soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⦿ Back ⦿", callback_data="SBACK"),
        InlineKeyboardButton(text="⦿ Close ⦿", callback_data="CLOSE"),
    ],
]

CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⦿ Back ⦿", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⦿ Close ⦿", callback_data="CLOSE"),
    ],
]

HELP_START = [
    [
        InlineKeyboardButton(text="« Help »", callback_data="HELP"),
        InlineKeyboardButton(text="🐳 Close 🐳", callback_data="CLOSE"),
    ],
]

HELP_BUTN = [
    [
        InlineKeyboardButton(text="« Features »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="⦿ Close ⦿", callback_data="CLOSE"),
    ],
]

ABOUT_BTN = [
    [
        InlineKeyboardButton(text="🎄 Support 🎄", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« Help »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🍾 Owner 🍾", user_id=OWNER),
    ],
    [
        InlineKeyboardButton(text="🐳 Updates 🐳", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="⦿ Back ⦿", callback_data="BACK"),
    ],
]
