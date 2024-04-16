from pyrogram.types import InlineKeyboardButton

import config
from TGNMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ʙᴇᴀᴜᴛʏ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="ʙᴏʏ ʙᴇsᴛɪᴇ", url=f"https://t.me/Idhayann"),
        ],
    ]
    return buttons
