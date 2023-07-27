# JUEGO DE PIEDRA PAPEL O TIJERAS
import random
def maquina():
    jugadas = ["PIEDRA","PAPEL","TIJERAS"]
    return random.choice(jugadas)  

def usuario():
    while True:
        elecusario=input("Elija: PIEDRA - PAPEL - TIJERAS\n").STRIP().upper()
        if elecusario in ["PIEDRA","PAPEL","TIJERAS"]:
            return elecusario
        else:
            print("Opción incorrecta. Pruebe de nuevo")

def partida():
    
    ganausuario=0
    ganamaquina=0
    while ganausuario<=2 and ganamaquina<=2:
        jmaquina=maquina()
        jusuario=usuario()
        if jmaquina=="PIEDRA":
            if jusuario=="TIJERAS":
                print("PIEDRA rompe TIJERAS, la máquina gana")
                ganamaquina +=1
            
            elif jusuario=="PAPEL":
                print("PAPEL embuelve PIEDRA, ganas tú")
                ganausuario +=1
            else:
                print("Empate")
            

        if jmaquina=="TIJERAS":
            if jusuario=="PAPEL":
                print("TIJERAS corta PAPEL, la máquina gana")
                ganamaquina +=1
            
            elif jusuario=="PIEDRA":
                print("PIEDRA ROMPE TIJERAS, ganas tú")
                ganausuario +=1
        
            else:
                print("Empate")

        if jmaquina=="PAPEL":
            if jusuario=="PIEDRA":
                print("PAPEL embuelve PIEDRA, la máquina gana")
                ganamaquina +=1
            
            elif jusuario=="TIJERAS":
                print("TIJERAS corta PAPEL, ganas tú")
                ganausuario +=1
        
            else:
                print("Empate")
        print(jmaquina,jusuario)
        print("MÁQUINA",ganamaquina,"TU",ganausuario)
    

    if ganausuario>ganamaquina:
        print("Eres un campeón")
    else:
        print("Eres un pringao, gana la máquina")
    
    sino="SI"
    while sino=="SI":
        sino=input("¿Quieres seguir juegando?: SI/NO\n").upper()
        if sino=="NO":
            print("Adios")
            break
        else:
            partida()
            
if __name__ == "__main__":
    print("¡Bienvenido al juego de piedra, papel o tijeras!")
    partida()


