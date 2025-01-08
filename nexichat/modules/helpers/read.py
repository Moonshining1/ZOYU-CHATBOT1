from config import OWNER_USERNAME, SUPPORT_GRP
from nexichat import nexichat
from pyrogram import Client, filters



START = '''```
๏ ѕυρєя ғᴀsτ【◖ 𝗖υτє 𝗭ογυ ◗ 】ϲнαᴛʙοᴛ ๏```

➤ Features:
﹥ Supports: Text, Stickers, Photos, Videos
﹥ Multi-language: /setlang
﹥ Chatbot On/Off: /chatbot
﹥ Create Chatbot: /clone
﹥ ID Chatbot: /idclone

Stats:
﹥ Users: {}
﹥ Chats: {}
﹥ Uptime: {}

╔═════════════════╗
║ ˹ ᴧʟʟ ʙσᴛ's ˼ ➪ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/The_Incricible/817)  
║ ˹ ᴅєᴠ ˼ ➪ [мɪcҡεʏ](https://t.me/LEGEND_MICKEY)                         
╚═════════════════╝
**'''

HELP_READ = '''```
**Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.  Iғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ ɪɴ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/ZOYU_SUPPORT).

Aʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ: /```**
"""'''

TOOLS_DATA_READ = '''```
๏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ๏```

➤ /start – Wake up the bot & get a welcome message.
➤ /help – List all commands & features.
➤ /ping – Check the bot’s response time.
➤ /id – Get User ID, Chat ID, & Message ID.
➤ /broadcast – Send a message to all chats.
➤ /shayri – Receive random shayari.
➤ /link (Group ID) – Get the group link.
➤ /givelink – Get the current group’s link.
➤ /repo – View the bot’s source code.

╔════════════════╗
║ Developer:  [мɪcҡεʏ](https://t.me/LEGEND_MICKEY) 
╚════════════════╝
'''

CHATBOT_READ = '''```
๏ ᴄʜᴀᴛʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ๏```

➤ /chatbot – Enable/Disable chatbot.
➤ /ask – Ask anything from ChatGPT.
➤ /setlang – Select chat language.
➤ /resetlang – Reset language to default.
➤ /chatlang – View current chat language.
➤ /status – Check chatbot status.
➤ /stats – Get bot stats.
➤ /clone [Token] – Clone your bot.
➤ /idclone [Session] – Create ID-specific chatbot.

📡 Developer:   [мɪcҡεʏ](https://t.me/LEGEND_MICKEY) 
'''

SOURCE_READ = '''```
๏ ѕυρєя ғᴀsτ【◖ 𝗖υτє 𝗭ογυ ◗ 】ϲнαᴛʙοᴛ ๏```

**❖ ʜᴇʀᴇ ᴏᴜʀ ᴀʟʟ ʙᴏᴛ ᴀʟɪᴠᴇ ᴀʟʟ ʙᴏᴛ ʀᴇᴘᴏ ɪs ᴘʀɪᴠᴀᴛᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ [˹ ᴧʟʟ ʙσᴛ's ˼](https://t.me/The_Incricible/817)**'''

ADMIN_READ = f"sᴏᴏɴ"

ABOUT_READ = f"""
**➻ [{nexichat.name}](https://t.me/{nexichat.username}) ɪs ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛ-ʙᴏᴛ.**
**➻ [{nexichat.name}](https://t.me/{nexichat.username}) ʀᴇᴘʟɪᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.**
**➻ ʜᴇʟᴘs ʏᴏᴜ ɪɴ ᴀᴄᴛɪᴠᴀᴛɪɴɢ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
**➻ ᴡʀɪᴛᴛᴇɴ ɪɴ [ᴘʏᴛʜᴏɴ](https://www.python.org) ᴡɪᴛʜ [ᴍᴏɴɢᴏ-ᴅʙ](https://www.mongodb.com) ᴀs ᴀ ᴅᴀᴛᴀʙᴀsᴇ**
**──────────────**
**➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ [{nexichat.name}](https://t.me/{nexichat.username})**
"""
