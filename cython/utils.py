from sys import *

from telethon import *

from . import *


def load_plugins(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import importlib
        from pathlib import Path

        path = Path(f"plugins/{plugin_name}.py")
        name = "plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        import importlib
        import sys
        from pathlib import Path

        from . import HNDLR, LOGS, udB, ultroid_bot
        from . import ultroid_bot as cipherxbot
        from .dB.database import Var
        from .misc import _supporter as xxx
        from .misc._assistant import (
            asst_cmd,
            callback,
            in_pattern,
            inline,
            inline_owner,
            owner,
        )
        from .misc._decorators import ultroid_cmd
        from .misc._wrappers import eod, eor

        path = Path(f"plugins/{plugin_name}.py")
        name = "plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.asst = ultroid_bot.asst
        mod.asst = cipherxbot.asst
        mod.tgbot = ultroid_bot.asst
        mod.tgbot = cipherxbot.asst
        mod.ultroid_bot = ultroid_bot
        mod.cipherxbot = cipherxbot
        mod.ultroid_bot = cipherxbot
        mod.bot = ultroid_bot
        mod.bot = cipherxbot
        mod.ultroid = ultroid_bot
        mod.ultroid = cipherxbot
        mod.owner = owner()
        mod.in_owner = inline_owner()
        mod.inline = inline()
        mod.in_pattern = in_pattern
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.ultroid_cmd = ultroid_cmd
        mod.on_cmd = ultroid_cmd
        mod.callback = callback
        mod.Redis = udB.get
        sys.modules["support"] = xxx
        sys.modules["userbot"] = xxx
        sys.modules["userbot.utils"] = xxx
        sys.modules["userbot.config"] = xxx
        spec.loader.exec_module(mod)
        sys.modules["plugins." + plugin_name] = mod
        try:
            PLUGINS.append(plugin_name)
        except BaseException:
            if plugin_name not in PLUGINS:
                PLUGINS.append(plugin_name)
            else:
                pass


# for addons


def load_addons(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import importlib
        from pathlib import Path

        path = Path(f"addons/{plugin_name}.py")
        name = "addons.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        import importlib
        import sys
        from pathlib import Path

        from . import HNDLR, LOGS, udB, ultroid_bot
        from . import ultroid_bot as cipherxbot
        from .dB.database import Var
        from .misc import _supporter as xxx
        from .misc._assistant import (
            asst_cmd,
            callback,
            in_pattern,
            inline,
            inline_owner,
            owner,
        )
        from .misc._decorators import ultroid_cmd
        from .misc._supporter import Config, admin_cmd, sudo_cmd
        from .misc._wrappers import eod, eor

        path = Path(f"addons/{plugin_name}.py")
        name = "addons.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.asst = ultroid_bot.asst
        mod.asst = cipherxbot.asst
        mod.tgbot = ultroid_bot.asst
        mod.tgbot = cipherxbot.asst
        mod.ultroid_bot = ultroid_bot
        mod.cipherxbot = cipherxbot
        mod.cipherxbot = cipherxbot
        mod.ultroid_bot = cipherxbot
        mod.ub = ultroid_bot
        mod.ub = cipherxbot
        mod.bot = ultroid_bot
        mod.bot = cipherxbot
        mod.ultroid = ultroid_bot
        mod.ultroid = cipherxbot
        mod.borg = ultroid_bot
        mod.borg = cipherxbot
        mod.telebot = ultroid_bot
        mod.telebot = cipherxbot
        mod.jarvis = ultroid_bot
        mod.jarvis = cipherxbot
        mod.friday = ultroid_bot
        mod.friday = cipherxbot
        mod.owner = owner()
        mod.in_owner = inline_owner()
        mod.inline = inline()
        mod.eod = eod
        mod.edit_delete = eod
        mod.LOGS = LOGS
        mod.in_pattern = in_pattern
        mod.hndlr = HNDLR
        mod.handler = HNDLR
        mod.HNDLR = HNDLR
        mod.CMD_HNDLR = HNDLR
        mod.Config = Config
        mod.Var = Var
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.asst_cmd = asst_cmd
        mod.ultroid_cmd = ultroid_cmd
        mod.on_cmd = ultroid_cmd
        mod.callback = callback
        mod.Redis = udB.get
        mod.admin_cmd = admin_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["ub"] = xxx
        sys.modules["var"] = xxx
        sys.modules["jarvis"] = xxx
        sys.modules["support"] = xxx
        sys.modules["userbot"] = xxx
        sys.modules["telebot"] = xxx
        sys.modules["fridaybot"] = xxx
        sys.modules["jarvis.utils"] = xxx
        sys.modules["uniborg.util"] = xxx
        sys.modules["telebot.utils"] = xxx
        sys.modules["userbot.utils"] = xxx
        sys.modules["userbot.events"] = xxx
        sys.modules["jarvis.jconfig"] = xxx
        sys.modules["userbot.config"] = xxx
        sys.modules["fridaybot.utils"] = xxx
        sys.modules["fridaybot.Config"] = xxx
        sys.modules["userbot.uniborgConfig"] = xxx
        spec.loader.exec_module(mod)
        sys.modules["addons." + plugin_name] = mod
        try:
            ADDONS.append(plugin_name)
        except BaseException:
            if plugin_name not in ADDONS:
                ADDONS.append(plugin_name)
            else:
                pass


# for assistant


def load_assistant(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import importlib
        from pathlib import Path

        path = Path(f"assistant/{plugin_name}.py")
        name = "assistant.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        import importlib
        import sys
        from pathlib import Path

        from . import HNDLR, udB, ultroid_bot
        from . import ultroid_bot as cipherxbot
        from .misc._assistant import asst_cmd, callback, in_pattern, inline_owner, owner
        from .misc._wrappers import eod, eor

        path = Path(f"assistant/{plugin_name}.py")
        name = "assistant.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.ultroid_bot = ultroid_bot
        mod.cipherxbot = cipherxbot
        mod.ultroid_bot = cipherxbot
        mod.ultroid = ultroid_bot
        mod.ultroid = cipherxbot
        mod.Redis = udB.get
        mod.udB = udB
        mod.bot = ultroid_bot
        mod.bot = cipherxbot
        mod.asst = ultroid_bot.asst
        mod.asst = cipherxbot.asst
        mod.owner = owner()
        mod.in_pattern = in_pattern
        mod.in_owner = inline_owner()
        mod.eod = eod
        mod.eor = eor
        mod.callback = callback
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.asst_cmd = asst_cmd
        spec.loader.exec_module(mod)
        sys.modules["assistant." + plugin_name] = mod


# msg forwarder


def load_pmbot(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import importlib
        from pathlib import Path

        path = Path(f"assistant/pmbot/{plugin_name}.py")
        name = "assistant.pmbot.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    else:
        import importlib
        import sys
        from pathlib import Path

        from . import HNDLR, udB, ultroid_bot
        from . import ultroid_bot as cipherxbot
        from .misc._assistant import asst_cmd, callback, owner
        from .misc._wrappers import eod, eor

        path = Path(f"assistant/pmbot/{plugin_name}.py")
        name = "assistant.pmbot.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.ultroid_bot = ultroid_bot
        mod.cipherxbot = cipherxbot
        mod.ultroid_bot = cipherxbot
        mod.ultroid = ultroid_bot
        mod.ultroid = cipherxbot
        mod.bot = ultroid_bot
        mod.bot = cipherxbot
        mod.Redis = udB.get
        mod.udB = udB
        mod.asst = ultroid_bot.asst
        mod.asst = cipherxbot.asst
        mod.owner = owner()
        mod.eod = eod
        mod.eor = eor
        mod.callback = callback
        mod.hndlr = HNDLR
        mod.HNDLR = HNDLR
        mod.asst_cmd = asst_cmd
        spec.loader.exec_module(mod)
        sys.modules["assistant.pmbot" + plugin_name] = mod
