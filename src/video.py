import json
import os
from googleapiclient.discovery import build

class Video:

    def __init__(self, video_id):
        self.video_id = video_id

        video_info = Video.get_service().videos().list(id=video_id, part='snippet,statistics').execute()
        json_format = json.loads(json.dumps((video_info)))

        self.video_title = json_format['items'][0]['snippet']['title']
        self.video_url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.views_count = json_format['items'][0]['statistics']['viewCount']
        self. likes_count = json_format['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.video_name

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)



class PLVideo(Video):

    def __init__(self, video_id, PL_id):
        self.video_id = video_id
        super().__init__(video_id)
        self.PL_id = PL_id
