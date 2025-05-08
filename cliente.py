import requests
import json
from app import LOCAl_IP
from app import DEFAULT_PORT


def main():
    URL = f"http://{LOCAl_IP}:{DEFAULT_PORT}/"
    response = requests.get(URL)
    tablero = response.json()
    # Print every call in console
    print(tablero)
    return tablero


if __name__ == "__main__":
    main()
