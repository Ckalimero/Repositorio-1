List = list()
Set = set()
l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del Set: "))
print("Introduzca los elementos de la lista:")
for i in range(0, l):
    List.append(int(input()))
print("Introduzca los elementos del Set: ")
for i in range(0, s):
    Set.add(int(input()))
print(List)
print(Set)



