from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("kec") & ~filters.private & ~filters.channel)
async def kec(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["kec"] < 3:
            oyun[m.chat.id]["kec"] += 1 
            await c.send_message(m.chat.id,f"❗ ᴄəᴍɪ 3 ᴋᴇᴄ̧ᴍᴇᴜ ʜᴀǫǫɪɴɪᴢ ᴠᴀʀ!\n➡️ sᴏ̈ᴢ ᴋᴇᴄ̧ɪşɪ ᴜɢ̆ᴜʀʟᴜᴅᴜʀ !\n✏️ ᴅᴜ̈ᴢɢᴜ̈ɴ sᴏ̈ᴢ : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 ʀᴀᴜɴᴅ : {oyun[m.chat.id]['round']}/60 
📝 sᴏ̈ᴢ :   <code>{kelime_list}</code>
💰 ǫᴀᴢᴀɴᴅɪɢ̆ɪɴɪᴢ xᴀʟ : 1
🔎 ᴋᴏ̈ᴍᴇᴋ : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 ᴜᴢᴜɴʟᴜɢ̆: {int(len(kelime_list)/2)} 

✏️ ǫᴀʀɪşɪɢ̆ ʜᴇʀғʟᴇʀᴅᴇɴ ᴅᴏɢ̆ʀᴜ sᴏ̈ᴢᴜ̈ ᴛᴀᴘɪɴ
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Kᴇᴄ̧ɪş ᴅᴜ̈ᴢɢᴜ̈ɴ ʏᴀᴅᴅᴀ ǫᴀʟᴅɪ! </code> \n ᴏʏᴜɴᴜ ᴅᴜʀᴅᴜʀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ /cancel ʏᴀᴢɪʙ ᴅᴀʏᴀɴᴅɪʀᴀ ʙɪʟᴇʀsᴇɴ✍🏻**")
    else:
        await m.reply(f"❗ **ɢʀᴜʙᴜɴᴜᴢᴅᴀ ᴏʏᴜɴ ᴏʏɴᴀɴᴍɪʀ!\n ʏᴇɴɪ ᴏʏᴜɴᴀ ʙᴀşʟᴀᴍᴀɢ̆ ᴜ̈ᴄ̧ᴜ̈ɴ /oyun ʏᴀᴢᴀ ʙɪʟᴇʀsᴇɴ✍🏻**")
