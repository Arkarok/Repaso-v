print("Tercer punto")

lista_1=[]

n=int(input("Digita la cantidad de valores que tendra la lista: "))
for i in range(0,n):
    an=int(input("Digita los valores de la lista: "))
    lista_1.append(an)

print(lista_1)

change=lista_1[::-1]

print(change)
