from pprint import pprint

import requests
# TASK 1
heroes_list = ['Hulk', 'Captain America', 'Thanos']
for heroes_name in heroes_list:
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{heroes_name}')
    heroes_intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
    best_intelligence = 0
    clever_hero = ''
    if heroes_intelligence > best_intelligence:
        best_intelligence = heroes_intelligence
        clever_hero = heroes_name
print(clever_hero, best_intelligence)

# def test_request():
#     url = "https://cloud-api.yandex.net/v1/disk/resources/files"
#     headers = {'Authorization': 'OAuth AQAAAAAFb6IVAADLW6pIWXkR-k0gsGDbokios1I', 'Content-Type': 'application/json'}
#     response = requests.get(url, headers=headers)
#     pprint(response.json())
#
# if __name__ == '__main__':
#     test_request()

# TASK 2

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        files = {'file': open('test_upload.txt', 'rb')}
        headers = {'Authorization': 'OAuth AQAAAAAFb6IVAADLW6pIWXkR-k0gsGDbokios1I',
                   'Content-Type': 'application/json'}
        response = requests.put(url=url, headers=headers, files=files)
        print(response.status_code)
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    uploader = YaUploader('test_upload.txt')
    result = uploader.upload()
    """ссылка на файл в компьютере"""
# 'C:\Users\79122\PycharmProjects\pythonProject\requests_test\test_upload.txt'