import os
import time
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger

from safety.tools import *
from telethon import __version__

from ..version import __version__ as __cython__
from ..version import ultroid_version

if os.path.exists("heartless.log"):
    os.remove("heartless.log")

LOGS = getLogger("Fenix Logs")
TeleLogger = getLogger("Telethon")
TeleLogger.setLevel(WARNING)

basicConfig(
    format="%(asctime)s || %(name)s [%(levelname)s] : %(message)s",
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
    handlers=[FileHandler("heartless.log"), StreamHandler()],
)

LOGS.info(
    """
                ---------------------------------------------------------
                               Starting UserBot Deployment
                ---------------------------------------------------------
"""
)


LOGS.info(f"Fenix Version - {__cython__}")
LOGS.info(f"Telethon Version - {__version__}")
LOGS.info(f"UserBot Version - {ultroid_version}")
