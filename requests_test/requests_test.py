from pprint import pprint

import requests

def test_request():
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization: OAuth AQAAAAAFb6IVAADLW6pIWXkR-k0gsGDbokios1I", "Content-Type: application/json"}
    response = requests.get(url, headers=headers)
    pprint(response.json())

if __name__ == '__requests_test__':
    test_request()
    