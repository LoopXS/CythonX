import re

import setuptools

requirements = [
    "redis",
    "python-decouple==3.3",
    "python-dotenv==0.15.0",
    "aiofiles",
    "aiohttp",
]


with open("cython/version.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "cython"
author = "CythonX"
description = "A Secure and Powerful Python-Telethon Based Library For CɪᴘʜᴇʀX Bot."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/LoopXS/CythonX"
project_urls = {
    "Source Code": "https://github.com/LoopXS/CythonX",
}
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

setuptools.setup(
    name=name,
    version=version,
    author=author,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    project_urls=project_urls,
    license=license,
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=classifiers,
    python_requires=">=3.6",
)
