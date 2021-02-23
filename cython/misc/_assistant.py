import functools
from telethon import events
from .. import *
from ..utils import *
from plugins import *
from telethon.tl.types import InputWebDocument

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id
ULTROID_PIC = "https://telegra.ph/file/167a0b85048b04129bd3b.jpg"
MSG = f"""
**CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ**
➖➖➖➖➖➖➖➖➖➖
**Owner**: [{OWNER_NAME}](tg://user?id={OWNER_NAME})
**✨ CɪᴘʜᴇʀX is the best ✨**
➖➖➖➖➖➖➖➖➖➖
"""

# decorator for assistant


def inline_owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in sed:
                await function(event)
            else:
                try:
                    builder = event.builder
                    sur = builder.article(
                        title="CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ",
                        url="https://t.me/Hackintush",
                        description="(c) CɪᴘʜᴇʀX",
                        text=MSG,
                        thumb=InputWebDocument(ULTROID_PIC, 0, "image/jpeg", []),
                        buttons=[
                            [Button.url("CɪᴘʜᴇʀX inbox", url="https://t.me/Hackintush")]
                        ]
                    )
                    await event.answer(
                        [sur],
                        switch_pm=f"🤖: Assistant of {OWNER_NAME}",
                        switch_pm_param="start",
                    )
                except BaseException:
                    pass

        return wrapper

    return decorator


def asst_cmd(dec):
    def ult(func):
        pattern = "^/" + dec  # todo - handlers for assistant?
        ultroid_bot.asst.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return ult


def callback(sed):
    def ultr(func):
        data = sed
        ultroid_bot.asst.add_event_handler(
            func, events.callbackquery.CallbackQuery(data=data)
        )

    return ultr


def inline():
    def ultr(func):
        ultroid_bot.asst.add_event_handler(func, events.InlineQuery)

    return ultr


def in_pattern(pat):
    def don(func):
        pattern = pat
        ultroid_bot.asst.add_event_handler(func, events.InlineQuery(pattern=pattern))

    return don


# check for owner
def owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in sed:
                await function(event)
            else:
                try:
                    await event.answer(f"This is {OWNER_NAME}'s bot.")
                except BaseException:
                    pass

        return wrapper

    return decorator
