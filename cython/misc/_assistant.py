import functools

from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.events import CallbackQuery, InlineQuery, NewMessage
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    InputWebDocument,
    PeerChannel,
)
from telethon.utils import get_display_name

from .. import asst, ultroid_bot
from . import owner_and_sudos

ULTROID_PIC = "https://telegra.ph/file/167a0b85048b04129bd3b.jpg"
MSG = f"""
**⚜️ CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ ⚜️**
✵✵✵✵✵✵✵✵✵✵✵✵✵✵
**Owner**: CɪᴘʜᴇʀX
**✨ CɪᴘʜᴇʀX is the best ✨**
✵✵✵✵✵✵✵✵✵✵✵✵✵✵
"""➖➖➖➖➖➖➖
"""

# decorator for assistant


def inline_owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in sed:
                try:
                    await function(event)
                except BaseException:
                    pass
            else:
                try:
                    builder = event.builder
                    sur = builder.article(
                        title="CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ",
                        url="https://t.me/CipherXBot",
                        description="(c) CɪᴘʜᴇʀX Ⲉⲭⲥⳑυⲋⲓⳳⲉ ⲃⲟⲧ",
                        text=MSG,
                        thumb=InputWebDocument(ULTROID_PIC, 0, "image/jpeg", []),
                        buttons=[
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
                        ],
                    )
                    await event.answer(
                        [sur],
                        switch_pm=f"🏴‍☠: Assistant of {OWNER_NAME}",
                        switch_pm_param="start",
                    )
                except BaseException:
                    pass

        return wrapper

    return decorator


def asst_cmd(dec):
    def ult(func):
        pattern = "^/" + dec  # todo - handlers for assistant?
        asst.add_event_handler(func, NewMessage(incoming=True, pattern=pattern))

    return ult


def callback(dat):
    def ultr(func):
        asst.add_event_handler(func, CallbackQuery(data=dat))

    return ultr


def inline():
    def ultr(func):
        asst.add_event_handler(func, InlineQuery)

    return ultr


def in_pattern(pat):
    def don(func):
        asst.add_event_handler(func, InlineQuery(pattern=pat))

    return don


# check for owner
def owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if str(event.sender_id) in owner_and_sudos():
                await function(event)
            else:
                try:
                    await event.answer(
                        f"This is {get_display_name(ultroid.me)} ᴇxᴄlusivᴇ ʙᴏᴛ"
                    )
                except BaseException:
                    pass

        return wrapper

    return decorator


async def admin_check(event):
    # Anonymous Admin Support
    if not event.sender_id and (
        isinstance(event.peer_id, PeerChannel)
        and str(event.peer_id.channel_id) in str(event.chat_id)
    ):
        return True
    if str(event.sender_id) in owner_and_sudos():
        return True
    try:
        perms = await event.client.get_permissions(event.chat_id, event.sender_id)
    except UserNotParticipantError:
        return False
    if isinstance(
        perms.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
    ):
        return True
    return False
