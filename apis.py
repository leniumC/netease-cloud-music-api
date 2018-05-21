from utils import *


# 获取听歌排行榜
def get_records(uid, get_all=True):
    base_url = 'http://music.163.com/weapi/v1/play/record?csrf_token='

    text = {
        'csrf_token': '',
        'uid': str(uid),
        'offset': '0',
        'type': '0'
    }
    if not get_all:
        text['type'] = '-1'

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索歌曲
def get_search_songs(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索艺术家
def get_search_artists(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '100'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索专辑
def get_search_albums(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '10'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索视频
def get_search_videos(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1014'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索歌词
def get_search_lyrics(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1006'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索歌单
def get_search_playlists(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1000'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索电台
def get_search_radios(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1009'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content


# 搜索用户
def get_search_users(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web?csrf_token='

    text = {
        'csrf_token': '',
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1002'
    }

    text = json.dumps(text).replace(' ', '')

    content = send_request(text, base_url)

    return content
