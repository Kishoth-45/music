#unitedbots #callsmusic #psychobots
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"[✨](https://telegra.ph/file/7d64cbd248accefb41ebd.jpg) Hey! This is the Music Assistant of [ANJAL](https://t.me/Godofanjalbot) Ask at @Godofanjalsupport")
  return                        
