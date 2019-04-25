import math

print("Segundo punto")
lista=[]

n=int(input("Digita que cantidad de valores tendra la lista: "))
for i in range(0,n):
    a=int(input("Digita los valores de la lista: "))
    lista.append(a)

print(lista)
pot=n
num=0
for x in range(0,n):
    v=lista[x]
    pot-=1
    m=v*math.pow(10,pot)
    num+=m

print(num)

n_final=(num+1)
print(n_final)

lista_2=[]

if n_final%math.pow(10,n)==0:
    for i in range(0,n+1):
        a=int(n_final/math.pow(10,n-i))
        b=a%10
        lista_2.append(b)

else:
    trinket=n_final
    con_1=0
    for i in range(0,n):
        a=int(trinket/math.pow(10,(n-1)-con_1))
        b=a*math.pow(10,(n-1)-con_1)
        trinket-=b
        lista_2.append(a)
        con_1+=1

print(lista_2)

