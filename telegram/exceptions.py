from . import DP_NAME_SEPARATOR

class GeneralException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class ReservedCharacter(GeneralException):
    def __init__(self):
        super().__init__(f"Reserved Characters: '{DP_NAME_SEPARATOR}' can not be used in the datapack name")

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