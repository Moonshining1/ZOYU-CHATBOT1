import requests
from MukeshAPI import api
from pyrogram import filters, Client
from pyrogram.enums import ChatAction
from nexichat import nexichat as app

async def fetch_response(user_input):
    try:
        response = api.gemini(user_input)
        result = response.get("results")
        if result:
            return result
    except Exception as e:
        return None

    try:
        base_url = "https://chatwithai.codesearch.workers.dev/?chat="
        response = requests.get(base_url + user_input)
        if response and response.text.strip():
            return response.text.strip()
        return "**Both Gemini and Chat with AI are currently unavailable**"
    except Exception as e:
        return "**Chatgpt is currently dead. Try again later.**"

@Client.on_message(filters.command(["gemini", "ai", "ask", "chatgpt"]))
async def gemini_handler(client, message):
    user_input = None

    if message.text.startswith(f"/gemini@{client.me.username}") and len(message.text.split(" ", 1)) > 1:
        user_input = message.text.split(" ", 1)[1]
    elif message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    elif len(message.command) > 1:
        user_input = " ".join(message.command[1:])
    else:
        await message.reply_text("Example: `/ask who is Narendra Modi`")
        return

    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    result = await fetch_response(user_input)

    if result:
        await message.reply_text(result, quote=True)
