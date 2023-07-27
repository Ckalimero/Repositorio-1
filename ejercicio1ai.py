import random

def maquina():
    jugadas = ["PIEDRA", "PAPEL", "TIJERAS"]
    return random.choice(jugadas)

def usuario():
    while True:
        elecusario = input("Elija: PIEDRA - PAPEL - TIJERAS\n").strip().upper()
        if elecusario in ["PIEDRA", "PAPEL", "TIJERAS"]:
            return elecusario
        else:
            print("Opción inválida. Intente nuevamente.")

def partida():
    reglas = {
        "PIEDRA": "TIJERAS",
        "TIJERAS": "PAPEL",
        "PAPEL": "PIEDRA"
    }

    ganausuario = 0
    ganamaquina = 0

    while ganausuario < 2 and ganamaquina < 2:
        jmaquina = maquina()
        jusuario = usuario()

        if jusuario == reglas[jmaquina]:
            print(f"{jmaquina} gana, la máquina gana")
            ganamaquina += 1
        elif jmaquina == reglas[jusuario]:
            print(f"{jusuario} gana, ganas tú")
            ganausuario += 1
        else:
            print("Empate")

        print("MÁQUINA", ganamaquina, "TU", ganausuario)

    if ganausuario > ganamaquina:
        print("¡Eres un campeón!")
    else:
        print("Eres un pringao, gana la máquina")

if __name__ == "__main__":
    print("¡Bienvenido al juego de piedra, papel o tijeras!")
    partida()
