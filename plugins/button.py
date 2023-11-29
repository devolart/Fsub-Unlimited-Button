# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB
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
    
    if num_force_sub <= 3:
        dynamic_buttons.append([
            InlineKeyboardButton(text=f"ᴊᴏɪɴ {key}", url=getattr(client, f'invitelink{key}'))
            for key in FORCE_SUB.keys()
        ])
    else:
        num_rows = num_force_sub // 3
        num_extra_buttons = num_force_sub % 3

        num_columns = 3 if num_extra_buttons == 0 else 2

        for i in range(num_rows):
            dynamic_buttons.append([
                InlineKeyboardButton(text=f"ᴊᴏɪɴ {key}", url=getattr(client, f'invitelink{key}'))
                for key in list(FORCE_SUB.keys())[i * num_columns:(i + 1) * num_columns]
            ])

        if num_extra_buttons > 0:
            dynamic_buttons.append([
                InlineKeyboardButton(text=f"ᴊᴏɪɴ {key}", url=getattr(client, f'invitelink{key}'))
                for key in list(FORCE_SUB.keys())[num_rows * num_columns:]
            ])

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
        
        if num_force_sub <= 3:
            dynamic_buttons.append([
                InlineKeyboardButton(text=f"ᴊᴏɪɴ {key}", url=getattr(client, f'invitelink{key}'))
                for key in FORCE_SUB.keys()
            ])
        else:
            num_rows = num_force_sub // 3
            num_extra_buttons = num_force_sub % 3

            num_columns = 3 if num_extra_buttons == 0 else 2

            for i in range(num_rows):
                dynamic_buttons.append([
                    InlineKeyboardButton(text=f"ᴊᴏɪɴ {key}", url=getattr(client, f'invitelink{key}'))
                    for key in list(FORCE_SUB.keys())[i * num_columns:(i + 1) * num_columns]
                ])

            if num_extra_buttons > 0:
                dynamic_buttons.append([
                    InlineKeyboardButton(text=f"ᴊᴏɪɴ {key}", url=getattr(client, f'invitelink{key}'))
                    for key in list(FORCE_SUB.keys())[num_rows * num_columns:]
                ])

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
