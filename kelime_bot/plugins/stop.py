from pyrogram import Client
from pyrogram import filters
from random import shuffle
from kelime_bot import USERNAME
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("cancel") & ~filters.private & ~filters.channel)
async def cancel(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}   :   {oyun[m.chat.id]['oyuncular'][i]} Bal")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** ᴛəʀəғɪɴᴅəɴ ᴏʏᴜɴ ᴅᴀʏᴀɴᴅɪʀɪʟᴅɪ\n\nᴏʏᴜɴᴀ ʙᴀşʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ /oyun ʏᴀᴢ\n\n 📝 xᴀʟ ᴛᴀʙʟᴏsᴜ  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
    
