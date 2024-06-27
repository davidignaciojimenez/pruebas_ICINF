dict={}
z=0
while z<5:
    pais=input("Ingrese un país: ")
    capital=input("Ingrese la capital del país ingresado: ")
    dict[pais]=capital
    z+=1
turista=input("Ingrese el nombre del turista: ")
paispro=input("Ingrese el país de procedencia del turista: ")
print("El turista con el nombre",turista, "viene del país",paispro,"y su capital es:",dict[paispro],".")