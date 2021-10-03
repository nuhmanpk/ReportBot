import pyrogram
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "ReportBot",
    bot_token=os.environ["BOT_TOKEN"],
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
)


@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text("Start Message Here")


@bughunter0.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def report(bot, message):
 if message.reply_to_message:
    chatid = message.chat.id
    reporter = message.from_user.id
    admins = await bot.get_chat_members(chat_id=chatid, filter="administrators")
    success=0
    for admin in admins:
        try:
            success +=1
            await message.reply_to_message.copy(f"{admin.user.id}")
            await bot.send_message(
                text=f""" Reporter : {reporter} \n 
                Message Link : {message.reply_to_message.link}""",
                chat_id=admin.user.id,
            )
        except:
            pass
    if success > 0 :
        await message.reply_text("Reported to Admins")

 else:
    return
bughunter0.run()

