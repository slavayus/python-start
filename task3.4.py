import requests
import re


def fun():
    a = input()
    b = input()
    res_a = requests.get(a)
    flag = 'No'
    if res_a.status_code == 200:
        for link in re.findall(r'href="(.*)"', res_a.text):
            res_b = requests.get(link)
            if res_b.status_code == 200 and b in re.findall(r'href="(.*)"', res_b.text):
                flag = 'Yes'
                break

    print(flag)


regex = r'^(?:https?:)?(?:ftp?:)?(?:\/\/)?(?:[^@\n]+@)?([^:\/\n]+)'
print(*sorted(
    set(re.search(regex, href).group(1) for href in
        re.findall(r'<a.*href=["\'](.*?)["\']', requests.get(input().strip()).text)
        if not href.startswith('..') and not href.startswith('/'))), sep='\n')

#
# for href in re.findall(r'<a.*href=["\'](.*)["\'].*>', requests.get('http://pastebin.com/raw/hfMThaGb').text):
#     print(href)
