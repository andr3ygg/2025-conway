import requests , json
from program import mostrar

URL = 'http://192.168.1.61:5000'
response = requests.get(URL)
#print(response.text)

tablero = response.json()
mostrar(tablero)
