import requests
import json
from program import mostrar
from app import LOCAl_IP
from app import DEFAULT_PORT
import socket


def main():
    URL = f'http://{LOCAl_IP}:{DEFAULT_PORT}/'
    print(URL)
    response = requests.get(URL)
    tablero = response.json()
    mostrar(tablero)


if __name__ == '__main__':
    main()
