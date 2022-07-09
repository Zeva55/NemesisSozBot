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
        InlineKeyboardButton("➕ Grubuna Ekle", url=f"http://t.me/karabakhsozBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("😝 Sahibim", url="https://t.me/Rowlyn"),
        InlineKeyboardButton("💬 Support", url="https://t.me/NemesisChat"),
    ]
])


START = """
**🏆 Salam, Sözləri Qarışığ Şəkildən Düzgün Tapmağ Oyununa Xoş Geldin..**

➤ Melumat üçün ⚡ /help Toxun. 
"""

HELP = """
**🐊 Əmrlər Menyusuna Xoş geldiniz.**
/oyun - Oyunu başladmağ Üçün..
/kec - Üç ədəd haqqınız mövcuddur, oyunu keçmek üçün.. 
/rating - Oyunçular arasındaki rəqabət melumatı..
/cancel - Oyundan çıxmağ üçün lazım olan əmrdir.. 
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
        await m.reply("**❗ Oyun Onsuzda Grubunuzda Davam Edir ✍🏻 \n Oyunu durdurmağ üçün  /cancel yazıb durdura bilersiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nSöz Tapmağ Oyunu Başladı .\n\nUğurlar !", reply_markup=kanal)
        
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
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığınız Xal: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluğ : {int(len(kelime_list)/2)} 

✏️ Qarışığ hərflərdən doğru sözü tapın
        """
        await c.send_message(m.chat.id, text)
        
