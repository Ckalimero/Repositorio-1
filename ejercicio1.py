def log(prefijo,*args):
    print(prefijo,*args, sep=separador)

prefijo=input("Escribe el prefijo que deseas: ")
separador=input("Que separador deseas: ")
log(prefijo,5,7)