import inspect
import re

from telethon import Button
from telethon.events import CallbackQuery, InlineQuery, NewMessage
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .. import LOGS, asst, ultroid_bot
from . import append_or_update, owner_and_sudos

ULTROID_PIC = "https://telegra.ph/file/167a0b85048b04129bd3b.jpg"
OWNER = get_display_name(ultroid_bot.me)

MSG = f"""
**⚜️ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ ⚜️**
✵✵✵✵✵✵✵✵✵✵✵✵✵✵
**Owner**: CɪᴘʜᴇʀX
**✨ CɪᴘʜᴇʀX is the best ✨**
✵✵✵✵✵✵✵✵✵✵✵✵✵✵
➖➖➖➖➖➖➖
"""
IN_BTTS=[
    [
        Button.url(
            "✵CɪᴘʜᴇʀX Ⲃⲟⲧ✵",
            url="https://t.me/CipherXBot",
        ),
        Button.url(
            "✵Suᴩᴩᴏrᴛ Chᴀnnᴇl✵", 
            url="https://t.me/FutureTechnologyOfficial"
        ),
    ]
]


# decorator for assistant


def asst_cmd(pattern=None, load=None, **kwargs):
    """Decorator for assistant's command"""
    name = inspect.stack()[1].filename.split("/")[-1].replace(".py", "")

    def ult(func):
        if pattern:
            kwargs["pattern"] = re.compile("^/" + pattern)
        asst.add_event_handler(func, NewMessage(**kwargs))
        if load is not None:
            append_or_update(load, func, name, kwargs)

    return ult


def callback(data=None, owner=False, **kwargs):
    """Assistant's callback decorator"""

    def ultr(func):
        async def wrapper(event):
            if owner and not str(event.sender_id) in owner_and_sudos():
                return await event.answer(f"This is {OWNER} ᴇxᴄlusivᴇ ʙᴏᴛ")
            try:
                await func(event)
            except Exception as er:
                LOGS.exception(er)

        asst.add_event_handler(wrapper, CallbackQuery(data=data, **kwargs))

    return ultr


def in_pattern(pattern=None, owner=False, **kwargs):
    """Assistant's inline decorator."""

    def don(func):
        async def wrapper(event):
            if owner and not str(event.sender_id) in owner_and_sudos():
                res = [
                    await event.builder.article(
                        title="CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ",
                        url="https://t.me/CipherXBot",
                        description="(c) CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ",
                        text=MSG,
                        thumb=InputWebDocument(ULTROID_PIC, 0, "image/jpeg", []),
                        buttons=IN_BTTS,
                    )
                ]
                return await event.answer(
                    res,
                    switch_pm=f"🏴‍☠: Assistant of {OWNER}",
                    switch_pm_param="start",
                )
            try:
                await func(event)
            except Exception as er:
                LOGS.exception(er)

        asst.add_event_handler(wrapper, InlineQuery(pattern=pattern, **kwargs))

    return don
