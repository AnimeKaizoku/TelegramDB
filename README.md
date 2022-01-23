# TelegramDB
A library which uses your telegram account as a database for your projects.

**Documentation**: [telegramdb.readthedocs.io](https://telegramdb.readthedocs.io/) 

[![pypi](https://img.shields.io/pypi/v/telegramdb.svg)](https://pypi.org/project/TelegramDB)
[![pyversion](https://img.shields.io/pypi/pyversions/telegramdb.svg)](https://pypi.org/project/TelegramDB)
[![downlaods](https://img.shields.io/pypi/dm/telegramdb)](https://pypistats.org/packages/telegramdb)
[![docs](https://readthedocs.org/projects/telegramdb/badge/?version=stable)](https://telegramdb.readthedocs.io/en/latest/)

## Basic Usage
```python
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
```

## Installation
You can install this library by using standard pip command.
```bash
pip install TelegramDB
```

## Requirements
- Python 3.6 or higher
- A telegram client

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update examples as appropriate.

## License
[![GPLv3](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.en.html)
<br>Licensed Under <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">GNU General Public License v3</a>
