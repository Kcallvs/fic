import requests

URL = 'http://127.0.0.1:8000/api/v1/'

r = requests.get(URL + 'areas/')
print(r.json())

r = requests.post(URL + 'area_cadastrar/', json={'nome': 'Eventos'})
print(r.status_code)