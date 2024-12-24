from config import OWNER_USERNAME, SUPPORT_GRP
from nexichat import nexichat
from pyrogram import Client, filters

START = """**
{} 𝚝𝚑𝚎 𝕤𝕦𝕡𝕖𝕣𝕘𝕒𝕤𝕥 𝕔𝕙𝕒𝕥𝕓𝕠𝕥 💞
    
➪ 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 𝚝𝚎𝚡𝚝, 𝚝𝚒𝚌𝚔𝚎𝚛, 𝚙𝚑𝚘𝚝𝚘, 𝚟𝚒𝚍𝚎𝚘...
➪ 𝚖𝚞𝚕𝚝𝚒-𝚕𝚊𝚗𝚐𝚞𝚊𝚐𝚎 𝟵𝚘𝚛 𝚎𝚊𝚌𝚑 𝚌𝚑𝚊𝚝 /setlang
➪ 𝚌𝚑𝚊𝚝𝚋𝚘𝚝 𝚎𝚗𝚊𝚋𝚕𝚎𝚍/𝚍𝚒𝚜𝚊𝚋𝚕𝚎𝚍 𝚋𝚢 /chatbot
➪ 𝚖𝚊𝚔𝚎 𝚢𝚘𝚞𝚛 𝚘𝚠𝚗 𝚌𝚑𝚊𝚝𝚋𝚘𝚝 𝚋𝚢 /clone
➪ 𝚖𝚊𝚔𝚎 𝚢𝚘𝚞𝚛 𝚒𝚍-𝚌𝚑𝚊𝚝𝚋𝚘𝚝 𝚋𝚢 /idclone
    
◉ 𝚝𝚘𝚝𝚊𝚕 𝚞𝚜𝚎𝚛𝚜 : {}
◉ 𝚝𝚘𝚝𝚊𝚕 𝚌𝚑𝚊𝚝𝚜 : {}
◉ 𝚞𝚙𝚝𝚒𝚖𝚎 » {}
    
╔════════════╗
║ ➛ 𝚖𝚢 𝚛𝚎𝚙𝚘 ➪ [click here](https://github.com/amritraj78/KING-CHATBOT)  
║ ➛ 𝚌𝚛𝚎𝚊𝚝𝚘𝚛 ➪ [Amrit](https://t.me/ll_KINGDOM_ll)
╚════════════╝
**"""

HELP_READ = f"""**
𝚌𝚕𝚒𝚌𝚔 𝚘𝚗 𝚝𝚑𝚎 𝚋𝚞𝚝𝚝𝚘𝚗s 𝚋𝚎𝚕𝚘𝚠 𝚏𝚘𝚛 𝚖𝚘𝚛𝚎 𝚒𝚗𝚏𝚘𝚛𝚖𝚊𝚝𝚒𝚘𝚗. 𝙸𝚏 𝚢𝚘𝚞'𝚛𝚎 𝚕𝚘𝚘𝚔𝚒𝚗𝚐 𝚏𝚘𝚛 𝙰𝙽𝚈 𝙴𝚇𝙰𝙼𝙿𝙻𝙴, 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚊𝚜𝚔 𝚑𝚎𝚛𝚎 𝚏𝚘𝚛 𝚊𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚌𝚎.**
All commands can be used with: /**"""

TOOLS_DATA_READ = f"""**
╮THE 𝕊𝕌𝕀𝕋𝔼 𝕆𝔽 𝕋𝕆𝕆𝕃𝕊:
    
➛ /start to wake up the bot and receive a welcome message!
────────────
➛ /help for getting details about all commands and features.
────────────
➛ /ping to check the response time (ping) of the bot!
────────────
➛ /speedtest check server speed
────────────
➛ /id to get your user id, chat id, and message id in one message.
────────────
➛ /broadcast to forward a message to all chats based on specified flags! Example: `/broadcast -user -pin help`
────────────
➛ /shayri get random shayri for love
────────────
➛ /link (group id) to get link of group
➛ /givelink to get that group link in which command is written (write in group)
────────────
➛ use /repo to get the source code of the bot!
────────────
**"""

CHATBOT_READ = f"""**
╮HERE ARE THE COMMANDS FOR CHATBOT:
    
➛ /chatbot - opens options to enable or disable the chatbot.
────────────
➛ /ask - ask anything from chatbot
────────────
➛ /lang, /language, /setlang - opens a menu to select the chat language.  
────────────
➛ /resetlang, /nolang - resets the bot's language to mixed language.
────────────
➛ /chatlang - get current using chat lang.
────────────
➛ /status - check chatbot active or not.
────────────
➛ /stats - get bot stats.
────────────
➛ /clone [ bot token ] - to clone your bot.
────────────
➛ /idclone [ pyrogram string session ] - to make id-chatbot.
────────────
📢 made by ➛ [Amrit](https://t.me/ll_KINGDOM_ll) 💞**
"""

SOURCE_READ = f"""**Hey, the source code of [{nexichat.name}](https://t.me/{nexichat.username}) is given below.**
**Please fork the repo to get updates: [click here](https://github.com/amritraj78/KING-CHATBOT)**
"""

ADMIN_READ = f"""soon"""

ABOUT_READ = f"""**
➛ [{nexichat.name}](https://t.me/{nexichat.username}) is an ai based chat-bot.
➛ [{nexichat.name}](https://t.me/{nexichat.username}) replies automatically to a user.
➛ helps you in activating your groups.
➛ written in [python](https://www.python.org) with [mongo-db](https://www.mongodb.com) as a database**
────────────
**Click on the buttons given below for getting help and info about [{nexichat.name}](https://t.me/{nexichat.username}).**
"""

Would you like to proceed with submitting a pull request with these changes?
