lista=[]
lista2=[]
z=0
while z<10:
    obj=int(input("Ingrese el precio de un objeto en dólares: "))
    lista.append(obj)
    z+=1
for x in lista:
    x*=950
    lista2.append(x)
print("Los precios ingresados en Dólares Estadounidenses:",lista)
print("Los precios ingresados en Pesos Chilenos:",lista2)
