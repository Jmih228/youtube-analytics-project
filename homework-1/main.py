import sys
sys.path.append(r'../src')
from channel import Channel
# такой усложненный импорт из-за того, что простое src.item мой пайчарм почему-то не видит


if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.print_info()

    """
{
  "kind": "youtube#channelListResponse",
  "etag": "H-pNprJMhplXi-NIAD9wFm1GCgQ",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "SNKCVH4AEdoqn_JbHJmmNTFzmLg",
      "id": "UC-OVMPlMA3-YCIeg4z5z23A",
      "snippet": {
        "title": "MoscowPython",
        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
        "customUrl": "@moscowdjangoru",
        "publishedAt": "2012-07-13T09:48:44Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "MoscowPython",
          "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
        },
        "country": "RU"
      },
      "statistics": {
        "viewCount": "2336446",
        "subscriberCount": "26200",
        "hiddenSubscriberCount": false,
        "videoCount": "689"
      }
    }
  ]
}
    """
# откорректировал докстринг, чтобы там была информация, которую выдает метод на момент выполнения задания
# не совсем понятно, что тестировать, потому что данные постоянно меняются
# только если выделить какие-то статические данные и проверять их
