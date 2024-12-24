from config import OWNER_USERNAME, SUPPORT_GRP
from nexichat import nexichat
from pyrogram import Client, filters

START = """**
🤖 This is the superfast chatbot 🚀

📁 Supports text, sticker, photo, video...
🌍 Multi-language for each chat /lang
⚙️ Chatbot enabled/disabled by /chatbot
🔄 You can clone/make chatbot by /clone
🔄 Make your ID-chatbot by /idclone

👥 Total users : {}
💬 Total chats : {}
⏱️ Uptime » {}

╔═════════════════╗
║ ➻ My repo ➪ [Click Here](https://github.com/amritraj78/KING-CHATBOT) 🎁                
╚═════════════════╝

➲ Add me in groups to use features.
**"""

HELP_READ = f"""**
Click on the buttons below for more information. If you're facing any problem you can ask in[...]

All commands can be used with: /**
"""

TOOLS_DATA_READ = f"""**
๏ Here are the commands for tools:

➻ /start to wake up the bot and receive a welcome message!
──────────────
➻ /help for getting details about all commands and features.
──────────────
➻ /ping to check the response time (ping) of the bot!
──────────────
➻ /speedtest check server speed
──────────────
➻ /id to get your user ID, chat ID, and message ID all in one message.
──────────────
➻ /broadcast to forward a message to all chats based on specified flags!\nExample: `/broadcast -user -pin hello[...]`
──────────────
➻ /shayri get random shayri for your love
──────────────
➻ /link (group ID) to get the link of group
➻ /givelink to get that group link in which command is written (write in group)
──────────────
➻ Use /repo to get the source code of the bot!
──────────────
➲ Add me in groups to use features.**
"""

CHATBOT_READ = f"""**
๏ Here are the commands for chatbot:

➻ /chatbot - opens options to enable or disable the chatbot.
──────────────
➻ /ask - ask anything from ChatGPT
──────────────
➻ /lang, /setlang - opens a menu to select the chat language.  
──────────────
➻ /resetlang, /nolang - resets the bot's language to mixed language.
──────────────
➻ /chatlang - get current using chat lang for chat.
──────────────
➻ /status - check chatbot active or not.
──────────────
➻ /stats - get bot stats
──────────────
➻ /clone [ bot token ] - to clone your bot.
──────────────
➻ /idclone [ pyrogram string session ] - to make ID-chatbot.
──────────────
➲ Add me in groups to use features.
**"""

SOURCE_READ = f"**Hey, the source code of [{nexichat.name}](https://t.me/{nexichat.username}) is given below. Please fork the repo for your own use.**"

ADMIN_READ = f"Soon"

ABOUT_READ = f"""
**➻ [{nexichat.name}](https://t.me/{nexichat.username}) is an AI-based chat-bot.**
**➻ [{nexichat.name}](https://t.me/{nexichat.username}) replies automatically to a user.**
**➻ Helps you in activating your groups.**
**➻ Written in [Python](https://www.python.org) with [Mongo-DB](https://www.mongodb.com) as a database**
**──────────────**
**➻ Click on the buttons given below for getting basic help and info about [{nexichat.name}](https://t.me/{nexichat.username}).**
"""
