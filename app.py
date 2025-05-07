from flask import Flask
import sys
import program
import socket

# Flask App
app = Flask(__name__)
# Crea un tablero para todo el tiempo de vida de la app
tablero = program.init()


@app.route("/")
def mostrar_tablero():
    # Traemos el tablero y lo actualizamos cada que se ejecute la raíz
    global tablero
    tablero = program.actualizar(tablero)
    return f"{tablero}"


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


LOCAl_IP = get_ipv4_address()
DEFAULT_PORT = 5000


def main():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=DEFAULT_PORT, debug=False)
