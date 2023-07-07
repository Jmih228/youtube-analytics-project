import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, __channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = __channel_id

        channel_info = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        json_format = json.loads(json.dumps((channel_info)))

        self.title = json_format['items'][0]['snippet']['title']
        self.description = json_format['items'][0]['snippet']['localized']['description']
        self.url = f'youtube.com/channel/{__channel_id}'
        self.subscribers = json_format['items'][0]['statistics']['subscriberCount']
        self.video_count = json_format['items'][0]['statistics']['videoCount']
        self.views_count = json_format['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscribers) + int(other.subscribers)

    def __sub__(self, other):
        return int(self.subscribers) - int(other.subscribers)

    def __lt__(self, other):
        return int(self.subscribers) < int(other.subscribers)

    def __le__(self, other):
        return int(self.subscribers) <= int(other.subscribers)

    def __gt__(self, other):
        return int(self.subscribers) > int(other.subscribers)

    def __ge__(self, other):
        return int(self.subscribers) >= int(other.subscribers)
    @property
    def channel_id(self):
        return self.__channel_id
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # откорректировал код этого метода с учетом нового класс метода get_service
        channel = Channel.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self,filename):
        with open(filename, "a", encoding='utf-8') as channel_atributes:
            print(json.dumps(self.__dict__), file=channel_atributes)
# В атрибуте "description" закодированная строка, не успеваю разобраться в чем проблема :D
# Прошу вашей помощи
