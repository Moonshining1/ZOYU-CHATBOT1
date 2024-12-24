import os
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.types import Message
from nexichat.idchatbot.helpers import is_owner

async def is_user_owner(client: Client, user_id):
    clone_id = (await client.get_me()).id
    return await is_owner(clone_id, user_id)

@Client.on_message(filters.command("givelink", prefixes=[".", "/"]))
async def give_link_command(client, message):
    if not await is_user_owner(client, message.from_user.id):
        await message.reply_text("You don't have permission to use this command on this bot.")
        return

    try:
        link = await client.export_chat_invite_link(message.chat.id)
        await message.reply_text(f"**Here's the invite link for this chat:**\n\n{link}")
    except ChatAdminRequired:
        await message.reply_text("**Error: I need to be an admin with invite link permissions to generate the link.**")
    except Exception as e:
        await message.reply_text(f"**Error:** {str(e)}")

@Client.on_message(filters.command(["link", "invitelink"], prefixes=["/", "!", "%", ",", ".", "@", "#"]))
async def link_command_handler(client: Client, message: Message):
    if not await is_user_owner(client, message.from_user.id):
        await message.reply_text("You don't have permission to use this command on this bot.")
        return

    if len(message.command) != 2:
        await message.reply("**Invalid usage. Correct format: /link group_id**")
        return

    group_id = message.command[1]
    file_name = f"group_info_{group_id}.txt"

    try:
        chat = await client.get_chat(int(group_id))

        if not chat:
            await message.reply("**Unable to get information for the specified group ID.**")
            return

        try:
            invite_link = await client.export_chat_invite_link(chat.id)
        except FloodWait as e:
            await message.reply(f"**FloodWait: {e.x} seconds. Retrying in {e.x} seconds.**")
            return

        group_data = {
            "id": chat.id,
            "type": str(chat.type),
            "title": chat.title,
            "members_count": chat.members_count,
            "description": chat.description,
            "invite_link": invite_link,
            "is_verified": chat.is_verified,
            "is_restricted": chat.is_restricted,
            "is_creator": chat.is_creator,
            "is_scam": chat.is_scam,
            "is_fake": chat.is_fake,
            "dc_id": chat.dc_id,
            "has_protected_content": chat.has_protected_content,
        }

        with open(file_name, "w", encoding="utf-8") as file:
            for key, value in group_data.items():
                file.write(f"{key}: {value}\n")

        await client.send_document(
            chat_id=message.chat.id,
            document=file_name,
            caption=f"**Here is the information for {chat.title}:**\n\n**The group information is as follows:**"
        )

    except Exception as e:
        await message.reply(f"**Error:** {str(e)}")
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)
