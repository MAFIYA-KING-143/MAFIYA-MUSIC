from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME
from SHUKLAMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✦ ᴡᴇʟᴄᴏᴍᴇ ғᴏʀ  ᴘʀᴏғᴇssᴏʀ sᴏᴜʀᴀʙʜ ʀᴇᴘᴏs !

✦ ᴍᴇʀᴀ ʟᴀɴᴅ ʟᴇ ʟᴇ༗

✦ ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ ʀᴀɴᴅɪ ᴋᴇ.

✦ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ༗.
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ＡＤＤ ＭＥ ＢＡＢＹ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/Friends_Chatting_Group_Friends_0"),
          InlineKeyboardButton("ＰＲＯＦＥＳＳＯＲ", url="https://t.me/SOURABH_OWNER"),
          ],
               [
                InlineKeyboardButton("ＰＲＯＦＥＳＳＯＲ ＮＥＴＷＯＲＫ", url="https://t.me/PROFESSOR_NETWORK"),

],
[
              InlineKeyboardButton("ＭＡＩＮ ＢＯＴ", url=f"https://t.me/ll_PROFESSOR_BOT"),
              InlineKeyboardButton("︎ＭＹ ＲＥＰＯ", url=f"https://smmpanel.apikey.online"),
              
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/205f3cf027a5a11f5f70e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/itzshukla/STRANGER-MUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/itzshukla/STRANGER-MUSIC) | [UPDATES](https://t.me/SHIVANSH474)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


