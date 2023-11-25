from pyrogram.enums import ParseMode

from SophiaXmusic import app
from SophiaXmusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
╔════❰𝐏𝐋𝐀𝐘𝐈𝐍𝐆❱═══❍⊱❁۪۪
◈ <b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>
◈ 𝐂𝐡𝐚𝐭 ➪ **{message.chat.title}**
◈ 𝐂𝐡𝐚𝐭 𝐈𝐝 ➪ `{message.chat.id}`
◈ 𝐔𝐬𝐞𝐫 ➪ **{message.from_user.mention}**
◈ 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ➪ **@{message.from_user.username}**
◈ 𝐈𝐝 ➪ `{message.from_user.id}`
◈ 𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤 ➪ **{chatusername}**
◈ 𝐒𝐞𝐚𝐫𝐜𝐡𝐞𝐝 ➪ `{message.text.split(None, 1)[1]}`
◈ 𝐁𝐲 ➪ **{streamtype} ▄ █ ▄ █ ▄**
╚═══❰ #𝐍𝐞𝐰𝐒𝐨𝐧𝐠 ❱══❍⊱❁۪۪"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
