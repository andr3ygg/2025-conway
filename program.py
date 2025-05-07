import os
from random import randint
from time import sleep


config = {
    "ancho": 7,
    "alto": 7
}


# Genera una lista de las dimensiones indicadas en config
def init():
    def estado():
        return 0 if randint(0, 5) else 1 # ?

    tablero = []
    for i in range(config["alto"]):
        tablero.append([estado() for i in range(config["ancho"])])
        # Añade un numero al tablero en base a el número de items en cada sublista (ancho)
    return tablero


def mostrar(tablero):
    for linea in tablero:
        for cell in linea:
            dibujo = "·" if not cell else "*"
            # Si es 0, lo pone como punto
            # Si es cualquier cosa excepto 0, lo pone como *
            print(f"{dibujo}", end="")
        print()
    print()


def actualizar(anterior):
    #sumas = [[] for line in range(len(anterior))]
    siguiente = [[] for line in range(len(anterior))]

    def suma_alrededor(y, x):
        """
        # Límite horizontal
        def lh(x):
            return x if x < config["ancho"] else 0

        # Límite vertical
        def lv(y):
            return y if y < config["alto"] else 0
        """
        suma = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i < 0 or i >= config["alto"] or j < 0 or j >= config["ancho"] or (i == y and j == x):
                    continue
                    # Si pasa del limite, entonces lo ignora
                suma += anterior[i][j]
                # Si no es una esquina, entonces suma todo lo de alrededor
        
        return suma

    for y in range(len(anterior)):
        for x in range(len(anterior[y])):
            vecinos = suma_alrededor(y, x)
            nuevo_estado = 0
            if vecinos == 2:
                nuevo_estado = anterior[y][x]
            if vecinos == 3:
                nuevo_estado = 1

            #sumas[y].append(vecinos)
            siguiente[y].append(nuevo_estado)


    return siguiente


def ejecutar():
    tablero = init()
    mostrar(tablero)
    tablero = actualizar(tablero)
    print(tablero)


def main():
    ejecutar()