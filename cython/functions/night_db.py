from .. import udB

try:
    eval(udB.get("NIGHT_CHATS"))
except BaseException:
    udB.set("NIGHT_CHATS", "[]")


def add_night(chat):
    chats = eval(udB.get("NIGHT_CHATS"))
    if chat not in chats:
        chats.append(chat)
        udB.set("NIGHT_CHATS", str(chats))
    return


def rem_night(chat):
    chats = eval(udB.get("NIGHT_CHATS"))
    if chat in chats:
        chats.remove(chat)
        udB.set("NIGHT_CHATS", str(chats))
    return


def night_grps():
    return eval(udB.get("NIGHT_CHATS"))
