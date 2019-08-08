import requests
import sys
import json


def fun():
    for line in sys.stdin:
        print('Interesting' if requests.get('http://numbersapi.com/{}/math?json=true'.format(int(line))).json()[
            'found'] else 'Boring')


client_id = '974dc50d6c80ebf15aa6'
client_secret = 'a0cc3a7a18383da26c32777e52f856c4'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком

datas = {}
for _ in range(15):
    v = requests.get('https://api.artsy.net/api/artists/' + str(input()), headers=headers)
    v.encoding = 'utf-8'
    datas[v.json()['birthday']] = v.json()['sortable_name']

datas = sorted(datas.items(), key=lambda x: (x[0], x[1]))

for data in datas:
    print(data[1])
