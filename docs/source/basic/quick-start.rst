.. _quick-start:

===========
Quick-Start
===========

Let's see a longer example to learn some of the methods that the library
has to offer. These are known as "friendly methods", and you should always
use these if possible.

.. code-block:: python

    import asyncio, logging
    from os import getenv
    from pyrogram import Client, idle, filters
    from pyrogram.types import Message
    from telegramdb import TelegramDB, DataPack, Member

    # Creating a telegram client
    client = Client("session_name", getenv("API_ID"), getenv("API_HASH"))
    client.start()

    # Creating a TelegramDB instance
    SESSION = TelegramDB(client, getenv("DB_CHAT_ID"), debug=True)

    # Basic Logging for debugging purpose
    LOG_FORMAT = "-> [TelegramDB Example] [%(levelname)s - %(asctime)s]: %(message)s"
    logging.basicConfig(
        format=LOG_FORMAT,
        handlers=[logging.StreamHandler()],
        level=logging.INFO,
    )

    # A new datapack class inherited from DataPack 
    class User(DataPack):
        # naming the datapack 
        __datapack_name__ = "user"

        # here we have defined all the members of this datapack
        id = Member(int, is_primary=True)
        name = Member(str)
        username = Member(str)

        def __init__(self, id, name=None, username=None):
            self.id = id
            self.name = name
            self.username = username

    # this intialises datapack with its primary keys
    SESSION.prepare_datapack(User)

    # insertion lock to avoid duplicate keys 
    INSERTION_LOCK = asyncio.Lock()

    async def save_user_data(id: int, name: str, username: str):
        async with INSERTION_LOCK:
            SESSION.commit(User(id, name, username))

    # this message handler will log users to our database
    @client.on_message(group=1)
    async def check_users(_, message: Message):
        if user := message.from_user:
            await save_user_data(user.id, user.first_name, user.username)

    # this message handler with command filter will be used to retrieve values from the database
    @client.on_message(filters=filters.command("info", prefixes="."))
    async def get_info(_, message: Message):
        args = message.text.split()
        if len(args) > 1:
            try:
                user_id = int(args[1])
            except BaseException:
                await message.reply("You didn't enter a valid user id!")
                return
        else:
            user_id = message.from_user.id
        user = User(user_id)
        if not SESSION.get(user):
            await message.reply("User not found in the database.")
            return
        await message.reply(f"""
        **User Info**

        **UserID**: `{user.id}`
        **Name**: `{user.name}`
        **Username**: `{user.username}`
        """)

    def main():
        idle()

    asyncio.get_event_loop().run_until_complete(main())


Here, we showed you how to initialize datapacks, commit data, 
and get values with the help of a user logging script.

You should make sure that you understand what the code shown here
does, take note on how methods are called and used and so on before
proceeding. We will see all the available methods later on.