from pyrogram import Client, filters
import requests
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from nexichat import db
from nexichat.idchatbot.helpers import languages
import asyncio

lang_db = db.ChatLangDb.LangCollection
message_cache = {}

async def get_chat_language(chat_id, bot_id):
    try:
        chat_lang = await lang_db.find_one({"chat_id": chat_id, "bot_id": bot_id})
        return chat_lang["language"] if chat_lang and "language" in chat_lang else None
    except Exception as e:
        print(f"Error: {e}")
        return None

@Client.on_message(filters.command("chatlang", prefixes=[".", "/"]))
async def fetch_chat_lang(client, message):
    try:
        chat_id = message.chat.id
        bot_id = client.me.id
        chat_lang = await get_chat_language(chat_id, bot_id)
        await message.reply_text(f"The language code being used for this chat is: {chat_lang}")
    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text(f"Error: {e}")

@Client.on_message(filters.text, group=4)
async def store_messages(client, message: Message):
    global message_cache

    try:
        chat_id = message.chat.id
        bot_id = client.me.id
        chat_lang = await get_chat_language(chat_id, bot_id)

        if not chat_lang or chat_lang == "nolang":
            if message.from_user and message.from_user.is_bot:
                return

            if chat_id not in message_cache:
                message_cache[chat_id] = []

            message_cache[chat_id].append(message)

            if len(message_cache[chat_id]) >= 30:
                history = "\n\n".join([f"Text: {msg.text}..." for msg in message_cache[chat_id]])
                user_input = f"""
                sentences list :-
                [
                {history}
                ]

                Above is a list of sentences. Each sentence could be in different languages. Analyze the language of each sentence separately and identify the dominant language used for each sentence. 
                Provide only the official language name with language code (like 'en' for English, 'hi' for Hindi) in this format:
                Lang Name :- ""
                Lang code :- ""
                Provide only overall [Lang Name and Lang Code] in the above format. Do not provide anything else.
                """
                base_url = "https://chatwithai.codesearch.workers.dev/?chat="
                try:
                    response = requests.get(base_url + user_input)
                    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Select Language", callback_data="choose_lang")]])
                    await message.reply_text(f"**Chat language detected for this chat:**\n\n{response.text}\n\n**You can set my language using /lang**", reply_markup=reply_markup)
                    message_cache[chat_id].clear()
                except Exception as e:
                    await message.reply_text(f"**Failed to detect chat language. Error:** {e}")
    except Exception as e:
        print(f"Error: {e}")
