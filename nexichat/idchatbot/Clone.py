import logging
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid, AccessTokenInvalid
from config import API_HASH, API_ID, OWNER_ID
from nexichat import nexichat as app, save_idclonebot_owner, db as mongodb

IDCLONES = set()
cloneownerdb = mongodb.cloneownerdb
idclonebotdb = mongodb.idclonebotdb

async def get_string_session(message):
    if len(message.command) > 1:
        return message.text.split("/idclone", 1)[1].strip()
    return None

async def handle_clone(message, string_session):
    mi = await message.reply_text("**Checking your String Session...**")
    try:
        ai = Client(
            name="VIPIDCHATBOT",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=str(string_session),
            no_updates=False,
            plugins=dict(root="nexichat.idchatbot"),
        )
        await ai.start()
        user = await ai.get_me()
        await save_idclonebot_owner(user.id, message.from_user.id)
        details = {
            "user_id": user.id,
            "username": user.username or user.first_name,
            "name": user.first_name,
            "session": string_session,
        }
        await idclonebotdb.insert_one(details)
        IDCLONES.add(user.id)
        total_clones = await idclonebotdb.count_documents({})
        await app.send_message(int(OWNER_ID), f"**#New_Clone**\n\n**User:** @{user.username}\n\n**Details:** {details}\n\n**Total Clones:** {total_clones}")
        await mi.edit_text(f"**Session for @{user.username} successfully cloned ✅.**\n**Remove clone by:** /delidclone\n**Check all cloned sessions by:** /idcloned")
    except AccessTokenInvalid:
        await mi.edit_text(f"**Invalid String Session. Please provide a valid pyrogram string session.:**")
    except PeerIdInvalid:
        await mi.edit_text(f"**Your session successfully cloned 👍**\n**You can check by /idcloned**\n\n**But please start me (@{app.username}) From owner id**")
    except Exception as e:
        logging.exception("Error during cloning process.")
        await mi.edit_text(f"**Invalid String Session. Please provide a valid pyrogram string session.:**\n\n**Error:** `{e}`")

@Client.on_message(filters.command(["idclone", "cloneid"], prefixes=["."]))
async def clone_txt(client, message):
    string_session = await get_string_session(message)
    if string_session:
        await handle_clone(message, string_session)
    else:
        await message.reply_text("**Provide a Pyrogram String Session after the .idclone **\n\n**Example:** `.idclone string session paste here`")

@Client.on_message(filters.command(["idcloned", "clonedid"], prefixes=[".", "/"]))
async def list_cloned_sessions(client, message):
    try:
        cloned_bots = idclonebotdb.find()
        cloned_bots_list = await cloned_bots.to_list(length=None)
        if not cloned_bots_list:
            await message.reply_text("**No sessions have been cloned yet.**")
            return

        total_clones = len(cloned_bots_list)
        text = f"**Total Cloned Sessions:** {total_clones}\n\n"
        for bot in cloned_bots_list:
            text += f"**User ID:** `{bot['user_id']}`\n"
            text += f"**Name:** {bot['name']}\n"
            text += f"**Username:** @{bot['username']}\n\n"

        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("**An error occurred while getting list of cloned id-chatbots**")

@Client.on_message(filters.command(["delidclone", "delcloneid", "deleteidclone", "removeidclone"], prefixes=["."]))
async def delete_cloned_session(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("**⚠️ Please provide the string session after the command.**\n\n**Example:** `.delidclone your string session here`")
            return

        string_session = " ".join(message.command[1:])
        ok = await message.reply_text("**Checking the session string...**")

        cloned_session = await idclonebotdb.find_one({"session": string_session})
        if cloned_session:
            await idclonebotdb.delete_one({"session": string_session})
            await ok.edit_text(f"**Your String Session has been removed from my database ✅.**\n\n**Your bot will off after restart @{app.username}**")
        else:
            await message.reply_text("**⚠️ The provided session is not in the cloned list.**")
    except Exception as e:
        await message.reply_text(f"**An error occurred while deleting the cloned session:** {e}")
        logging.exception(e)

@Client.on_message(filters.command("delallidclone", prefixes=[".", "/"]) & filters.user(int(OWNER_ID)))
async def delete_all_cloned_sessions(client, message):
    try:
        a = await message.reply_text("**Deleting all cloned sessions...**")
        await idclonebotdb.delete_many({})
        IDCLONES.clear()
        await a.edit_text("**All cloned sessions have been deleted successfully ✅**")
    except Exception as e:
        await a.edit_text(f"**An error occurred while deleting all cloned sessions:** {e}")
        logging.exception(e)
