import asyncio
from pyrogram import Client, filters
from nexichat.idchatbot.helpers import is_owner

SPAM_CHATS = []

@Client.on_message(filters.command(["all", "mention", "tagall", "mentionall"], prefixes=["."]))
async def tag_all_users(client, message):
    clone_id = (await client.get_me()).id
    user_id = message.from_user.id
    if not await is_owner(clone_id, user_id):
        await message.reply_text("You don't have permission to use this command on this bot.")
        return
    
    if message.chat.id in SPAM_CHATS:
        await message.reply_text("Tagging process is already running. Use /cancel to stop.")
        return
    
    text = message.text.split(None, 1)[1] if len(message.command) > 1 else None
    if not text and not message.reply_to_message:
        await message.reply_text("Please provide text to tag all, like » `.all Hi Friends`")
        return
    
    SPAM_CHATS.append(message.chat.id)
    usernum = 0
    usertxt = ""
    try:
        async for m in client.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 3:
                await client.send_message(message.chat.id, f"{text}\n{usertxt}\n\n|| ➥ Off tagging by » /cancel ||")
                await asyncio.sleep(5)
                usernum = 0
                usertxt = ""
        if message.reply_to_message:
            await message.reply_to_message.reply_text(usertxt)
        else:
            await client.send_message(message.chat.id, f"{text}\n{usertxt}\n\n|| ➥ Off tagging by » /cancel ||")
    finally:
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass

@Client.on_message(filters.command([
    "stopmention", "stoptagall", "canceltagall", "offall", "cancel",
    "allstop", "stopall", "cancelmention", "offmention", "mentionoff",
    "alloff", "cancelall", "allcancel"
], prefixes=[".", "/"]))
async def cancelcmd(client, message):
    chat_id = message.chat.id
    
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        await message.reply_text("Tagging process successfully stopped!")
    else:
        await message.reply_text("No process ongoing!")
