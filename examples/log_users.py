# TelegramDB
# Copyright (C) 2022
# Anony <github.com/anonyindian>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio, logging
from os import getenv
from pyrogram import Client, idle, filters
from pyrogram.types import Message
from telegram import TelegramDB, DataPack, Member

client = Client("session_name", getenv("API_ID"), getenv("API_HASH"))
client.start()

SESSION = TelegramDB(client, getenv("DB_CHAT_ID"), debug=True)

LOG_FORMAT = "-> [TelegramDB Example] [%(levelname)s - %(asctime)s]: %(message)s"
logging.basicConfig(
    format=LOG_FORMAT,
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)

class User(DataPack):
    __datapack_name__ = "user"

    id = Member(int, is_primary=True)
    name = Member(str)
    username = Member(str)

    def __init__(self, id, name=None, username=None):
        self.id = id
        self.name = name
        self.username = username

SESSION.prepare_datapack(User)

def save_user_data(id: int, name: str, username: str):
    SESSION.commit(User(id, name, username))

@client.on_message(group=1)
def check_users(_, message: Message):
    if user := message.from_user:
        save_user_data(user.id, user.first_name, user.username)

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


