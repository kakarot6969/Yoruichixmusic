from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

repo_caption = """**
🤡 Dᴇᴀʀ Lᴏʀᴜ, - 

Tᴀʀɪ Mᴀᴀ Kɪ Cʜᴜᴛ Mᴀᴅʜᴇʀᴄʜᴏᴅ... Nᴏɪ Mɪʟᴀ Gᴀ Rᴇᴘᴏ
sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴍᴇʜ ʙʜᴇᴇᴋ ᴍᴀɴɢ ʟᴀᴡ#ᴅᴇ ᴋᴇʜ ᴅᴇᴠʟᴏᴘᴇʀ 🖕
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
            InlineKeyboardButton("💬 𝗕𝗛𝗘𝗘𝗞 𝗠𝗔𝗡𝗚", url="https://t.me/Alpha_Bots_Support"),
            InlineKeyboardButton("🛠️ 𝗨𝗣𝗗𝗔𝗧𝗘 𝗟𝗘𝗛 𝗠𝗖", url="https://t.me/Alpha_Bots_Updates")
        ],
        [
            InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/Evokakarot")
        ]
    reply_markup = InlineKeyboardMarkup(buttons)

    try:  
        await msg.reply_photo(
            photo="https://files.catbox.moe/0aa3v4.jpg",
            caption=repo_caption,
            reply_markup=reply_markup
        )
    except:
        pass
