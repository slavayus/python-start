from _datetime import *
# print((date(*map(lambda x: int(x), input().split(' '))) + timedelta(days=int(input()))).strftime("%-Y %-m %-d"))

from simplecrypt import encrypt, decrypt, DecryptionException
import urllib
from urllib import request

encrypted = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
print(encrypted)
passwords = urllib.request.urlopen(
    'https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()
print(passwords)
for x in passwords:
    try:
        print(x.strip())
        print(decrypt(x.strip(), encrypted)).decode('utf8')
    except DecryptionException:
        print('EE')
