lista=[]
cont=0
contnota=0
while True:
    nota=float(input("Ingrese una nota: "))
    if nota==0:
        break
    contnota+=nota
    lista.append(nota)
    cont+=1
print(len(lista))
print(contnota/cont)
lista.sort()
print(lista[0])
print(lista[-1])