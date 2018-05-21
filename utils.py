import os
from Crypto.Cipher import *
from binascii import hexlify
import base64

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'referer': 'http://music.163.com/user/home?id=253838290'
}
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
pub_key = '010001'
nonce = '0CoJUm6Qyw8W8jud'

def create_secret_key(size):
    key = hexlify(os.urandom(size))
    return key.decode('ascii')


def rsa_encrypt(text, pub_key):
    text = text[::-1]
    rs = int(hexlify(text.encode('ascii')), 16) ** int(pub_key, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def aes_encrypt(text, sec_key=nonce):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(sec_key, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext.decode('ascii')
