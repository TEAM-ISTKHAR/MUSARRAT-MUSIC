
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("ᴧɪ | ᴄʜᴧᴛɢᴘᴛ", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("ǫυσᴛʟʏ", callback_data="mplus HELP_Q"),InlineKeyboardButton("sᴛɪᴄᴋєʀs", callback_data="mplus HELP_Sticker")],         
    [InlineKeyboardButton("ᴛᴧɢᴧʟʟ", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("ɢιτнυϐ", callback_data="mplus HELP_Github"),InlineKeyboardButton("єxᴛʀᴧ", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("αcƭเσɳ", callback_data="mplus HELP_Action"),InlineKeyboardButton("sєᴧʀᴄʜ", callback_data="mplus HELP_Search"),InlineKeyboardButton("˹ ᴘʀσϻσᴛɪση ˼", callback_data="mplus HELP_Promotion")],    
    [InlineKeyboardButton("ғσηᴛ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("ᴄσµρℓεร", callback_data="mplus HELP_Couples"),InlineKeyboardButton("ɢʀᴧᴘʜ", callback_data="mplus HELP_TG")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]
