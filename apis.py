from utils import *
import requests
import json

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
    sec_key = create_secret_key(8)

    tmp = aes_encrypt(text)
    enc_text = aes_encrypt(tmp, sec_key)
    enc_sec_key = rsa_encrypt(sec_key, pub_key)

    data = {
        'params': enc_text,
        'encSecKey': enc_sec_key
    }

    print(json.dumps(data, indent=4))

    response = requests.post(base_url, data, headers=headers)
    content = json.loads(response.content.decode('utf-8'))

    return content
