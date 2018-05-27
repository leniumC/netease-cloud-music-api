from utils import *
from bs4 import BeautifulSoup


# 获取听歌排行榜
def get_user_records(uid, get_all=True):
    base_url = 'http://music.163.com/weapi/v1/play/record'

    data = {
        'uid': str(uid),
        'offset': '0',
        'type': '0'
    }

    if not get_all:
        data['type'] = '-1'

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 获取用户歌单
def get_user_playlists(uid, limit=10):
    base_url = 'http://music.163.com/weapi/user/playlist'

    data = {
        'limit': str(limit),
        'offset': '0',
        'uid': str(uid),
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索歌曲
def get_search_songs(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索艺术家
def get_search_artists(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '100'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索专辑
def get_search_albums(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '10'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索视频
def get_search_videos(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1014'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索歌词
def get_search_lyrics(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1006'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索歌单
def get_search_playlists(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1000'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索电台
def get_search_radios(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1009'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 搜索用户
def get_search_users(keyword, limit=10):
    base_url = 'http://music.163.com/weapi/cloudsearch/get/web'

    data = {
        'limit': str(limit),
        'offset': '0',
        's': keyword,
        'type': '1002'
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content


# 获取歌单信息
def get_playlist_info(id):
    base_url = 'http://music.163.com/playlist'
    
    data = {
        'id': str(id)
    }

    content = send_request(base_url, data, 'GET')
    soup = BeautifulSoup(content, 'lxml')

    play_count = soup.find('strong', {'id': 'play-count'}).text
    track_count = soup.find('span', {'id': 'playlist-track-count'}).text

    result = dict()
    result['play_count'] = play_count
    result['track_count'] = track_count

    track_data = soup.find('ul', {'class': 'f-hide'})
    tracks = []

    for a in track_data.find_all('a'):
        sid = a['href'][9:]
        name = a.text
        tracks.append({'id': sid, 'name': name})

    result['tracks'] = tracks

    return result


# 获取歌曲评论
def get_song_comments(id, limit=10):
    base_url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(id)

    data = {
        'rid': 'R_SO_4_' + str(id),
        'total': 'true',
        'limit': str(limit)
    }

    data = json.dumps(data).replace(' ', '')

    content = send_enc_request(data, base_url)

    return content
