from funciones import quiz_1

numb=[]
while True:

    n=int(input("Digita un valor v:"))
    if n>0 and n!=0:
        numb.append(n)
    if n==0:
        break

print(numb)

mayor=quiz_1.N_mayor(numb)
print("El numero mayor dentro de la lista fue de: ",mayor)
menor=quiz_1.N_menor(numb)
print("El numero menor dentro de la lista fue de: ",menor)
