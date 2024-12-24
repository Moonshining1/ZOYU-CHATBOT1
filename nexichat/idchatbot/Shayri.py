import random
from pyrogram import Client, filters
from pyrogram.types import Message

SHAYRI = [
    " 🌺**बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।**🌺 \n\n**🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀** ",
    " 🌺**मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।**🌺 \n\n**🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀** ",
    " 🌺**तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।**🌺 \n\n**🥀Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.🥀** ",
    " 🌺**काश वो दिन जल्दी आए, जब तू मेरे साथ सात फेरो में बन्ध जाए।**🌺 \n\n**🥀Kash woh din jldi aaye Jb tu mere sath 7 feron me bndh jaye.🥀** ",
    " 🌺**अपना हाथ मेरे दिल पर रख दो और अपना दिल मेरे नाम कर दो।**🌺 \n\n**🥀apna hath mere dil pr rakh do aur apna dil mere naam kar do.🥀** ",
    " 🌺**महादेव ना कोई गाड़ी ना कोई बंगला चाहिए सलामत रहे मेरा प्यार बस यही दुआ चाहिए।**🌺 \n\n**🥀Mahadev na koi gadi na koi bangla chahiye salamat rhe mera pyar bas yahi dua chahiye.🥀** ",
    # Additional shayari lines...
]

SHAYRI_COMMAND = ["gf", "bf", "shayri", "sari", "shari", "love"]

@Client.on_message(filters.command(SHAYRI_COMMAND, prefixes=[".", "/"]))
async def shayri(client: Client, message: Message):
    try:
        await message.reply_text(text=random.choice(SHAYRI))
    except Exception as e:
        await message.reply_text(f"Error: {e}")
