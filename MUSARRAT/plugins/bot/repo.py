from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MUSARRAT import app
from config import BOT_USERNAME
from MUSARRAT.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗧ᴇᴀᴍ 𝗣ᴜʀᴠɪ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰  @THUNDERDEVS  
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/THUNDERDEVS"),
          InlineKeyboardButton("⍣ ፝֠֩ ‌ ‌ꭘⷪ ‌ ꯭፝֠֩‌ ꯭‌ ‌‌𝚰𝛅꯭𝗍ᴋ꯭ʜᴧ꯭ꝛ", url="https://t.me/CRAZY_OP_02"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗣ᴜʀᴠɪ 𝗕ᴏᴛs", url=f"https://t.me/PURVI_SUPPORT"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/PURVI_MUSIC_BOT"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://files.catbox.moe/u8ih4t.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )