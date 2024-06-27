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
print("Cantidad de notas en la lista:",len(lista))
print("Promedio de las notas en la lista:",contnota/cont)
lista.sort()
print("Nota ingresada más baja:",lista[0])
print("Nota ingresada más alta:",lista[-1])
