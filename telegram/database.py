import inspect
from ast import literal_eval
from telethon import TelegramClient
from pyrogram import Client
from typing import Union
from . import DP_NAME_SEPARATOR
from .exceptions import InvalidClient, InvalidDataPack, ReservedCharacter, UnsupportedClient

class Member:
    def __init__(self, _:type, is_primary:bool=False):
        self.is_primary = is_primary
        return

class DataPack:
    __datapack_name__:str

    def __get_dict__(self):
        __dict_to_return = self.__dict__
        if '__datapack_name__' in __dict_to_return:
            __dict_to_return.pop('__datapack_name__')
        return __dict_to_return
    
    def __query_data__(self):
        return f"{self.__datapack_name__}: {self.__get_dict__()}"


class TelegramDB:
    __datapacks__:dict = {str:{"id":int, "data":str}}
    __dp_cache__:dict = {}
    def __init__(self, client: Union[Client, TelegramClient], chat_id: Union[int, str]=None, show_logs=True):
        if chat_id:
            self.__chat_id__ = chat_id
        else:
            self.__make_chat__(client)
        self.show_logs = show_logs
        self.__telegram_client__ = client
        self.__get_datapacks__(client)
        if show_logs:
            print("""
    TelegramDB Copyright (C) 2022 anonyindian
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.
            """)
    
    def prepare_datapack(self, datapack_class: DataPack):
        for i in inspect.getmembers(datapack_class):
            if not i[0].startswith('_') and not inspect.ismethod(i[1]):
                if isinstance(i[1], Member) and i[1].is_primary:
                    if self.show_logs:
                        print("-> Initialised", datapack_class, "with primary key", f"'{i[0]}'")
                    self.__dp_cache__[datapack_class] = i[0]
    
    # COMMIT
    def commit(self, datapack: DataPack):
        if DP_NAME_SEPARATOR in datapack.__datapack_name__:
            raise ReservedCharacter()
        datapack = self.__fill_datapack(datapack)
        self.__publish_data__(datapack, self.__format_datapack__(datapack))
    
    def __publish_data__(self, datapack: DataPack, data:str):
        if client := self.__telegram_client__:
            msg_id = 0
            if datapack.__datapack_name__ in self.__datapacks__:
                msg_id:int = self.__datapacks__[datapack.__datapack_name__]["id"]
            if isinstance(client, Client):
                if msg_id == 0:
                    msg_id = client.send_message(chat_id=self.__chat_id__, text=data).message_id
                    self.__commit_success__ = True
                else:
                    try:
                        client.edit_message_text(chat_id=self.__chat_id__, message_id=msg_id, text=data)
                        self.__commit_success__ = True
                    except:
                        self.__commit_success__ = False
                        if self.show_logs:
                            print("-> Failed to update:", datapack.__query_data__())
            elif isinstance(client, TelegramClient):
                if msg_id == 0:
                    msg_id = client.send_message(entity=self.__chat_id__, message=data, parse_mode=None).message_id
                    self.__commit_success__ = True
                else:
                    try:
                        client.edit_message(entity=self.__chat_id__, message=msg_id, text=data, parse_mode=None)
                        self.__commit_success__ = True
                    except:
                        self.__commit_success__ = False
                        if self.show_logs:
                            print("-> Failed to update:", datapack.__query_data__())
            else:
                raise InvalidClient()
            if self.show_logs and self.__commit_success__:
                print("->", datapack.__query_data__())
            self.__datapacks__[datapack.__datapack_name__] = {"id": msg_id, "data":datapack.__get_dict__()}
    
    # GET
    def get(self, datapack: DataPack, primary_member_value=None):
        datapack.__datapack_name__ += DP_NAME_SEPARATOR + str(primary_member_value)
        if datapack.__datapack_name__ in self.__datapacks__:
            return datapack(**self.__datapacks__[datapack.__datapack_name__]["data"])

    # UTILS
    def __format_datapack__(self, datapack: DataPack):
        query = f"#{datapack.__datapack_name__}"
        query += f"\n{datapack.__get_dict__()}"
        return query

    def __get_datapacks__(self, client: Union[Client, TelegramClient]):
        if isinstance(client, Client):
            from pyrogram.types import Message
            for message in client.iter_history(self.__chat_id__):
                message: Message = message
                if not message.text:
                    continue
                try:
                    text = message.text.markdown.split("\n", 1)
                    self.__datapacks__[text[0][1:]] = {"id":message.message_id, "data":literal_eval(text[1])}
                except:
                    raise InvalidDataPack(message.message_id)
                
        elif isinstance(client, TelegramClient):
            raise UnsupportedClient("telethon")
        else:
            raise InvalidClient()
    
    def __make_chat__(self, client: Union[Client, TelegramClient]):
        if isinstance(client, Client):
            chat = client.create_channel("Telegram DB")
            self.__chat_id__ = chat.id
        elif isinstance(client, TelegramClient):
            raise UnsupportedClient("telethon")
        else:
            raise InvalidClient()
    
    def __fill_datapack(self, datapack: DataPack):
        for dp in self.__dp_cache__:
            if isinstance(datapack, dp):
                datapack.__datapack_name__ += f"{DP_NAME_SEPARATOR}" + str(getattr(datapack, self.__dp_cache__[dp]))
                break
        return datapack