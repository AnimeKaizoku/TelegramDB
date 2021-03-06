.. _authorizing:

===========
Authorizing
===========

Before working with TelegramDB, you need to create your Telegram Client using 
`Pyrogram <https://github.com/pyrogram/pyrogram>`_ or `Telethon <https://github.com/lonamiwebs/telethon>`_ 

- Using Pyrogram

.. code-block:: python

    from pyrogram import Client

    client = Client(
        "my_account",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef"
    )

- Using Telethon

.. code-block:: python

    from telethon.sync import TelegramClient

    # Use your own values from my.telegram.org
    api_id = 12345
    api_hash = '0123456789abcdef0123456789abcdef'

    # The first parameter is the .session file name (absolute paths allowed)
    client = TelegramClient('anon', api_id, api_hash)


.. note::

    This API ID and hash is the one used by *your application*, not your
    phone number. You can use this API ID and hash with *any* phone number
    or even for bot accounts.


Editing the Code
================

This is a little introduction for those new to Python programming in general.

We will write our code inside ``hello.py``, so you can use any text
editor that you like. To run the code, use ``python3 hello.py`` from
the terminal.

.. important::

    Don't call your script ``telegramdb.py``! Python will try to import
    the client from there and it will fail with an error such as
    "ImportError: cannot import name 'TelegramDB' ...".


Creating TelegramDB
===================

We can finally initialize the telegram database!

.. code-block:: python

    from telegramdb import TelegramDB
    from pyrogram import Client

    client = Client(
        "my_account",
        api_id=12345,
        api_hash="0123456789abcdef0123456789abcdef"
    )
    chat_id = 777000
    SESSION = TelegramDB(client, chat_id)


In the first line, we import the class name so we can create an instance
of the client and in the second line we imported the Pyrogram Client. Then, we define variables to store pyrogram client instance. 

At last, we create a new :class:`telegramdb.TelegramDB`
instance and call it ``SESSION``. We can now use the SESSION
for anything that we want, such as committing a datapack to storage chat.


Authorizin as a Bot Account
===========================

Right now you can not use TelegramDB for a bot account due to 
telegram's limitations but we expect to add their support soon.