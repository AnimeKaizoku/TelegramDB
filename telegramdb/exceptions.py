# TelegramDB
# Copyright (C) 2023
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

from . import DP_NAME_SEPARATOR

class GeneralException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class ReservedCharacter(GeneralException):
    def __init__(self, name:str = None):
        super().__init__(f"Reserved Characters: '{DP_NAME_SEPARATOR}' can not be used in the datapack name: '{name}'")

class InvalidDataPack(GeneralException):
    def __init__(self, message_id: int=None):
        msg = "Invalid DataPack"
        if message_id:
            msg += f": Found an invalid DataPack at message id '{message_id}' of the database chat"
        super().__init__(msg)

class UnsupportedClient(GeneralException):
    def __init__(self, message=None):
        msg = "Unsupported Client"
        if message:
            msg += f": {msg}"
        super().__init__(msg)

class InvalidClient(GeneralException):
    def __init__(self):
        super().__init__("Invalid Client: provided client not valid")