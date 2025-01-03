from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from nexichat import OWNER, nexichat


START_BOT = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="˹ ᴅєᴠ ˼", user_id=OWNER),
        InlineKeyboardButton(text="˹ sυᴘᴘσʀᴛ ˼", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="˹ ғᴇᴀᴛᴜʀᴇs ˼", callback_data="HELP"),
    ],
]


DEV_OP = [
    [
        InlineKeyboardButton(text="˹ ᴅєᴠ ˼", user_id=OWNER),
        InlineKeyboardButton(text="˹ sυᴘᴘσʀᴛ ˼", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅ ˼", callback_data="HELP"),
    ],
    [
        # InlineKeyboardButton(text="˹ ʀєᴘσ ˼", callback_data="SOURCE"),
        InlineKeyboardButton(text="˹ ᴧʙօυᴛ ˼", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
            url=f"https://t.me/{nexichat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="⌯ ᴄʟσsє ⌯",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙαck ⌯", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="˹ cнαƭʙοƭ ˼", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="˹ ᴛσσʟs ˼", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="˹ εɳαɓʟε ˼", callback_data="enable_chatbot"),
        InlineKeyboardButton(text="˹ ᴅɪѕαʙʟε ˼", callback_data="disable_chatbot"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="˹ sᴏᴏɴ ˼", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙαck ⌯", callback_data="SBACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="⌯ ʙαck ⌯", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅ ˼", callback_data="HELP"),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅ ˼", url=f"https://t.me/{nexichat.username}?start=help"
        ),
        InlineKeyboardButton(text="⌯ ᴄʟσsє ⌯", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="˹ sυᴘᴘσʀᴛ ˼", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="˹ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅ ˼", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="˹ ᴅєᴠ ˼", user_id=OWNER),
        #   InlineKeyboardButton(text="˹ ʀєᴘσ ˼", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="˹ υᴘᴅᴧᴛєs ˼", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="⌯ ʙαck ⌯", callback_data="BACK"),
    ],
]
