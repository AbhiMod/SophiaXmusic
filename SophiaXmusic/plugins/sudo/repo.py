import asyncio

from pyrogram import filters

import config
from SophiaXmusic import app
from SophiaXmusic.utils.formatters import convert_bytes





@app.on_message(filters.command("repo"))
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.."
    )
    up_r = f"[ʀᴇᴘᴏ](https://github.com/AbhiModszYT?tab=repositories)"
    sp_c = f"[𝘽𝙤𝙩 𝙉𝙚𝙬𝙨](t.me/AMBOTYT)"
    sp_g = f"[𝗔𝗠 𝗦𝘂𝗽𝗽𝗼𝗿𝘁](t.me/AM_YTSUPPORT)"
    ow_i = f"[𝗔𝗠𝗕𝗢𝗧](https://t.me/AM_YTBOTT)"

 ##############
 
    text = f"""ꜱᴏᴘʜɪᴀ ᴍᴜꜱɪᴄ ʀᴇᴘᴏ ⌫

    
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎ 𝗔𝗠𝗕𝗢𝗧:</u>

𝗥𝗘𝗣𝗢 ❥︎ {up_r}

𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❥︎ {sp_c}

𝗚𝗥𝗢𝗨𝗣 ❥︎ {sp_g}

𝗢𝗪𝗡𝗘𝗥 ❥︎ {ow_i}

    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
