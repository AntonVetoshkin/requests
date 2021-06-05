
# PREPARE_UPLOAD_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
# params = {'path': '/9.txt', 'overwrite': 'true'}
# TOKEN = 'OAuth AQAAAAAFb6IVAADLW6pIWXk'
# headers = {'Accept': 'application/json', 'Authorization': TOKEN}
#
# file_path = 'recipes.txt'
#
# response = requests.get(PREPARE_UPLOAD_URL, params=params, headers=headers)
# print(response.text)
#
# put_url = response.json().get('href')
# print(put_url)
#
# files = {'file': open(file_path, 'rb')}
# response = requests.put(put_url, files=files, headers=headers)
# print(response)