.. TelegramDB documentation master file, created by
   sphinx-quickstart on Sat Jan 22 13:28:55 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TelegramDB's documentation!
======================================

.. toctree::
   :hidden:
   :caption: First Steps

   basic/installation
   basic/authorizing
   basic/quick-start
   basic/next-steps

.. toctree::
   :hidden:
   :caption: Documentation

   tgdb/telegramdb
   tgdb/datapack
   tgdb/member

.. code-block:: python

   from os import getenv
   from pyrogram import Client
   from telegramdb import TelegramDB, DataPack, Member

   client = Client("session_name", getenv("API_ID"), getenv("API_HASH"))
   client.start()
   SESSION = TelegramDB(client, getenv("DB_CHAT_ID"))

   class TestData(DataPack):
      __datapack_name__ = "test"

      id = Member(int, is_primary=True)
      name = Member(str)

      def __init__(self, id):
         self.id = id

   SESSION.prepare_datapack(TestData)

   test = TestData(777000)
   test.name = "Telegram"
   SESSION.commit(test)

TelegramDB is a modern python library which uses your 
telegram account to store database for your projects.

Requirements
============

- Python version >= 3.6
- A telegram client (`Pyrogram <https://github.com/pyrogram/pyrogram>`_ or `Telethon <https://github.com/lonamiwebs/telethon>`_)

Contributing
============

Repository: https://github.com/AnimeKaizoku/TelegramDB

Pull requests are always welcome. For major changes, 
please open an issue first to discuss what you would like to change.

Please make sure to update examples as appropriate.

License
=======

.. image:: https://www.gnu.org/graphics/gplv3-127x51.png
  :alt: GPL v3

Licensed Under `GNU General Public License v3 <https://www.gnu.org/licenses/gpl-3.0.en.html>`_