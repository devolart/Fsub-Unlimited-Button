# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB, BUTTONS_PER_ROW, BUTTONS_JOIN_TEXT
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB:
        buttons = [
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons

    dynamic_buttons = []
    num_force_sub = len(FORCE_SUB)

    current_row = []
    for key in FORCE_SUB.keys():
        current_row.append(InlineKeyboardButton(text=f"{BUTTONS_JOIN_TEXT} {key}", url=getattr(client, f'invitelink{key}')))
        if len(current_row) == BUTTONS_PER_ROW:
            dynamic_buttons.append(current_row)
            current_row = []

    if current_row:
        dynamic_buttons.append(current_row)

    buttons = [
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
        ],
    ] + dynamic_buttons + [
        [InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close")],
    ]
    return buttons

def fsub_button(client, message):
    if FORCE_SUB:
        dynamic_buttons = []
        num_force_sub = len(FORCE_SUB)

        current_row = []
        for key in FORCE_SUB.keys():
            current_row.append(InlineKeyboardButton(text=f"{BUTTONS_JOIN_TEXT} {key}", url=getattr(client, f'invitelink{key}')))
            if len(current_row) == BUTTONS_PER_ROW:
                dynamic_buttons.append(current_row)
                current_row = []

        if current_row:
            dynamic_buttons.append(current_row)

        try:
            dynamic_buttons.append([
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ])
        except IndexError:
            pass

        return dynamic_buttons
