import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "cython"
version = "1.0.0"
author = "CythonX"
description = "A Secure and Powerful Python-Telethon Based Library For CɪᴘʜᴇʀX Bot."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/CipherX1-ops/cython"

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
    install_requires=[
        "telethon>=1.19.5",
        "redis",
        "python-decouple==3.3",
        "cryptg",
        "python-dotenv==0.15.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
