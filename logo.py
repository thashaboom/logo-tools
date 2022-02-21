from pyrogram import filters
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("9963698"))
API_HASH = os.environ.get("f0da0af0ccf385757281ff9ac8f0810b")
BOT_TOKEN = os.environ.get("5247938467:AAGz2l3vRDt3eXYknHCmVGrtxh_UC5a-VBs")

logo = Client("logo Bot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)


caption = """
✍️ Logo Created Successfully✔️

◇───────────────◇

🚀 **Created By** : **[LOGO GENERATE BOT 🔅](http://t.me/shalilogogenarator_bot)**

🌺 **Requestor** : ** {} **

🌀 **Powered By **  : **[ 🎶EDM MŰ§ÏČ PŁÅČƏ.🇱🇰 ](https://t.me/nonstopedm)**

◇───────────────◇️  
    """
#◇───────────────────────────────────────◇ 

START_BUTTONS=[
    [
        InlineKeyboardButton('🎶EDM MŰ§ÏČ PŁÅČƏ.🇱🇰', url='https://t.me/nonstopedm'),
        InlineKeyboardButton('🚀 Support Group 🚀', url='https://t.me/nonstopedm'),
    ],
    [InlineKeyboardButton('🌺 Github Repository 🌺', url='ඒවා දෙන්න බැ අනේ')],
]

#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("start"))
async def start(client,message):
    await message.reply("🌀 Hi I am Logo Generate Bot Telegram...",
    reply_markup=START_BUTTONS)

#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logo?name={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌀 Open In Google 🌀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇────────────────────────────────────◇ 
  
@logo.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logohq?name={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌀 Open In Google 🌀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#◇──────────────────────────────────────◇ 

@logo.on_message(filters.command("write"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    API = "https://api.single-developers.software/write"
    body = {     
     "text":f"{text}"     
    }
    req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)
    img = req.history[1].url
    await app.send_photo(message.chat.id, photo=img, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌀 Open In Google 🌀", url=f"{img}"
                    )
                ]
            ]
          ),
    )

#◇───────────────────────────────────────────◇

@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/wallpaper?search={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌀 Open In Google 🌀", url=f"{photo}"
                    )
                ]
            ]
          ),
    )


logo.run()
