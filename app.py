from flask import Flask
import sys
sys.path.append("C:/Users/Andrey/Documents/clones/")
import program
   ## FLASK APP
app = Flask(__name__)

tablero = program.init()

@app.route("/", methods=["GET", "POST"])
def hello_world():
    global tablero
    #program.mostrar(tablero)
    tablero = program.actualizar(tablero)
    return f'{tablero}'

if __name__ == '__main__':
    app.run(host="192.168.1.61" , port=5000, debug=False)
