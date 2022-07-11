from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ ǫʀᴜʙᴀ ᴇʟᴀᴠᴇ ᴇᴛ", url=f"http://t.me/nemesissozbot?startgroup=new")
    ],
    [
        InlineKeyboardButton("😝 sᴀʜɪʙɪᴍ", url="https://t.me/Rowlyn"),
        InlineKeyboardButton("💬 ᴅᴇsᴛᴇᴋ ɢʀᴜʙᴜ", url="https://t.me/NemesisChat"),
    ]
])


START = """
**🏆 Sᴀʟᴀᴍ, Sᴏ̈ᴢʟəʀɪ Qᴀʀɪşɪɢ̆ şəᴋɪʟᴅəɴ ᴅᴜ̈ᴢɢᴜ̈ᴍ ғᴏʀᴍᴀᴅᴀ ᴛᴀᴘᴍᴀɢ̆ Oʏᴜɴᴜɴᴀ xᴏş ɢᴇʟᴅɪɴ**

➤ ᴍᴇʟᴜᴍᴀᴛ ᴜ̈ᴄ̧ᴜ̈ɴ ⚡ /help ʏᴀᴢ 
"""

HELP = """
**🐊 Əᴍʀʟəʀ ᴍᴇɴʏᴜsᴜɴᴀ xᴏş ɢᴇʟᴍɪsɪɴɪᴢ.**
/oyun - ᴏʏᴜɴᴜ ʙᴀşʟᴀᴅᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ..
/kec - ᴋᴇᴄ̧ᴍᴇᴋ ᴜ̈ᴄ̧ᴜ̈ɴ, 3 əᴅəᴅ ᴋᴇᴄ̧ᴍᴇᴋ ʜᴀǫǫɪɴɪᴢ ᴠᴀʀᴅɪʀ
/rating - ᴏʏᴜɴᴄ̧ᴜʟᴀʀ ᴀʀᴀsɪɴᴅᴀᴋɪ ʀəǫᴀʙəᴛ ᴍᴇʟᴜᴍᴀʀɪ
/cancel - ᴏʏᴜɴᴅᴀɴ ᴄ̧ɪxᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ ʟᴀᴢɪᴍ ᴏʟᴀɴ əᴍʀᴅɪʀ.. 
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyun")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ ᴏʏᴜᴍ ᴏɴsᴜᴢᴅᴀ ɢʀᴜʙᴜɴᴜᴢᴅᴀ ᴅᴀᴠᴀᴍ ᴇᴅɪʀ ✍🏻 \n ᴏʏᴜɴᴜ ᴅᴀʏᴀɴᴅɪʀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ  /cancel ʏᴀᴢᴍᴀɢ̆ɪᴠɪᴢ ᴋɪғᴀʏᴇᴛᴅɪʀ")
    else:
        await m.reply(f"**{m.from_user.mention}** ᴛəʀəғɪɴᴅəɴ! \nsᴏ̈ᴢᴜ̈ ᴛᴀᴘᴍᴀɢ̆ ᴏʏᴜɴᴜ ʙᴀşʟᴀᴅɪ .\n\nᴜɢ̆ᴜʀʟᴀʀ !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 ʀᴀᴜɴᴅ : {oyun[m.chat.id]['round']}/30
📝 sᴏ̈ᴢ :   <code>{kelime_list}</code>
💰 ǫᴀᴢᴀɴᴅɪɢ̆ɪɴɪᴢ  xᴀʟ: 1
🔎 ᴋᴏ̈ᴍᴇᴋ: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 ᴜᴢᴜɴʟᴜɢ̆ : {int(len(kelime_list)/2)} 

✏️ ǫᴀʀɪşɪɢ̆ ᴠᴇʀɪʟᴍɪş ʜᴇʀᴅʟᴇʀᴅᴇɴ ᴅᴏɢ̆ʀᴜ sᴏ̈ᴢᴜ̈ ᴛᴀᴘɪɴ
        """
        await c.send_message(m.chat.id, text)
        
