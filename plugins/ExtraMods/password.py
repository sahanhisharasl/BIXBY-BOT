# Copyright (C) 2023 DX-MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

import random, os
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import PREFIX

@Client.on_message(filters.command(["genpassword", 'genpw'], PREFIX))
async def password(bot, update):
    message = await update.reply_text(text="`Pʀᴏᴄᴇꜱꜱɪɴɢ..`")
    password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    if len(update.command) > 1:
        qw = update.text.split(" ", 1)[1]
    else:
        ST = ["5", "7", "6", "9", "10", "12", "14", "8", "13"] 
        qw = random.choice(ST)
    limit = int(qw)
    random_value = "".join(random.sample(password, limit))
    txt = f"<b>Lɪᴍɪᴛ:</b> {str(limit)} \n<b>Pᴀꜱꜱᴡᴏʀᴅ: <code>{random_value}</code>"
    btn = InlineKeyboardMarkup([[InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇꜱ', url='https://t.me/dxmodsupdates')]])
    await message.edit_text(text=txt, reply_markup=btn, parse_mode=enums.ParseMode.HTML)
