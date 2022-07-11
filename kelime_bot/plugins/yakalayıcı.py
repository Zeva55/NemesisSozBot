from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import rating
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *









@Client.on_message(filters.text & ~filters.private & ~filters.channel)
async def buldu(c:Client, m:Message):
    global oyun
    global rating
    try:
        if m.chat.id in oyun:
            if m.text.lower() == oyun[m.chat.id]["kelime"]:
                await c.send_message(m.chat.id,f"🤍 ᴛəʙʀɪᴋʟəᴅ !\n**{m.from_user.mention}** \n**<code>{oyun[m.chat.id]['kelime']}</code>** , sᴏ̈ᴢᴜ̈ɴᴜ̈ ᴛᴀᴘᴅɪ ✅")
                if f"{m.from_user.mention}" in rating:
                    rating[f"{m.from_user.mention}"] += 1
                else:
                    rating[f"{m.from_user.mention}"] = 1
                
                try:
                    puan = oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)]
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] +=1
                except KeyError:
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = 1
                
                
                oyun[m.chat.id]["kelime"] = kelime_sec()
                oyun[m.chat.id]["round"] = oyun[m.chat.id]["round"] + 1
                
                if not oyun[m.chat.id]["round"] <= 60:
                    siralama = []
                    for i in oyun[m.chat.id]["oyuncular"]:
                        siralama.append(f"{i} :   {oyun[m.chat.id]['oyuncular'][i]}  Bal")
                    siralama.sort(reverse=True)
                    siralama_text = ""
                    for i in siralama:
                        siralama_text += i + "\n"
                    
                    return await c.send_message(m.chat.id,f"✅ ᴏʏᴜɴ sᴏɴʟᴀɴᴅɪʀɪʟᴅɪ \n\n📝 ǫᴀᴢᴀɴɪʟᴀɴ xᴀʟʟᴀʀ :\n\n{siralama_text}\n\n ʏᴇɴɪ ᴏʏᴜɴ ᴜ̈ᴄ̧ᴜ̈ɴ  /oyun ʏᴀᴢ !")
                
                
                
                kelime_list = ""
                kelime = list(oyun[m.chat.id]['kelime'])
                shuffle(kelime)
                for harf in kelime:
                    kelime_list+= harf + " "
            
                text = f"""
🎯 ʀᴀᴜɴᴅ : {oyun[m.chat.id]['round']}/60 
📝 sᴏ̈ᴢ :   <code>{kelime_list}</code>
💰 ǫᴀᴢᴀɴᴅɪɢ̆ɪɴɪᴢ xᴀʟ: 1
🔎 ᴋᴏ̈ᴍᴇᴋ: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 ᴜᴢᴜɴʟᴜɢ̆ : {int(len(kelime_list)/2)} 

✏️ǫᴀʀɪşɪɢ̆ ʜəʀғʟəʀᴅəɴ ᴅᴏɢ̆ʀᴜ sᴏ̈ᴢᴜ̈ ᴛᴀᴘɪɴ
                        """
                await c.send_message(m.chat.id, text)
    except KeyError:
        pass
    
    
gonderilmedi = True
data_message = None
EKLENEN_CHATS = []
@Client.on_message()
async def data(c:Client, m:Message):
    global EKLENEN_CHATS
    global gonderilmedi
    global data_message
    
    chat_id = str(m.chat.id)
    
    if chat_id in EKLENEN_CHATS:
        return

    if gonderilmedi:
        data_message= await c.send_message(OWNER_ID, f"{OWNER_ID}")
        gonderilmedi = False
        
    
    else:
        chats = await c.get_messages(OWNER_ID, data_message.message_id)
        chats = chats.text.split()
        
        if chat_id in chats:
            pass
        else:
            chats.append(chat_id)
            EKLENEN_CHATS.append(chat_id)
            data_text = ""
            for i in chats:
                data_text += i + " "
            await c.edit_message_text(OWNER_ID, data_message.message_id, data_text)
            
            
