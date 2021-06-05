from pprint import pprint
# import requests
# TASK 1
# heroes_list = ['Hulk', 'Captain America', 'Thanos']
# for heroes_name in heroes_list:
#     response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{heroes_name}')
#     heroes_intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
#     best_intelligence = 0
#     clever_hero = ''
#     if heroes_intelligence > best_intelligence:
#         best_intelligence = heroes_intelligence
#         clever_hero = heroes_name
# print(clever_hero, best_intelligence)

# def test_request():
#     url = "https://cloud-api.yandex.net/v1/disk/resources/files"
#     TOKEN =
#     headers = {'Authorization': 'OAuth TOKEN, 'Content-Type': 'application/json'}
#     response = requests.get(url, headers=headers)
#     pprint(response.json())
#
# if __name__ == '__main__':
#     test_request()

# TASK 2
import requests

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        PREPARE_UPLOAD_URL = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path':'test_upload.txt', 'overwrite': 'true'}
        TOKEN = 'OAuth ****************************************'
        headers = {'Accept': 'application/json', 'Authorization': TOKEN}

        response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
        put_url = response.json().get('href')

        files = {'file': open(self.file_path, 'rb')}
        response = requests.put(put_url, files=files, headers=headers)
        if response.status_code == 201: print('File successfully uploaded.')

if __name__ == '__main__':
    uploader = YaUploader('test_upload.txt')
    result = uploader.upload()

