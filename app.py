from flask import Flask
import main as game
import socket

app = Flask(__name__)


def get_ipv4_address():
    # Connect to an external host; doesn't actually send data
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # This IP doesn't need to be reachable;
        # just used to determine the local IP
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# Constants for client
LOCAl_IP = get_ipv4_address()
DEFAULT_PORT = 5000

# Crea un tablero para todo el tiempo de vida de la app
tablero = game.init()


@app.route("/")
def mostrar_tablero():
    global tablero
    # tablero = game.actualizar(tablero)
    # tablero = game.mostrar(tablero)
    tablero = game.actualizar(tablero)
    return f"{tablero}"


# Not working yet
@app.route("/actualizar")
def actualizar_tablerto():
    global tablero
    tablero = game.actualizar(tablero)
    return f"{tablero}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=DEFAULT_PORT, debug=False)
