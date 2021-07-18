import re

import setuptools

with open("cython/version.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "cython"
version = "1.0.0"
author = "CythonX"
description = "A Secure and Powerful Python-Telethon Based Library For CɪᴘʜᴇʀX Bot."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/CipherX1-ops/cython"

classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]
requirements = [
    "redis",
    "python-decouple==3.3",
    "py-tgcalls==0.5.2",
    "python-dotenv==0.15.0",
    "cloudscraper",
    "aiofiles",
    "aiohttp",
]

setuptools.setup(
    name=name,
    version=version,
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    license=license,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=classifiers,
    python_requires=">=3.6",
)
