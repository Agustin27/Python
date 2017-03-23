print ("--intervalo de n numeros entre 20 y 60--")
print (" ")

try:
    num=int(input("ingrese la cantidad de numeros a usar en el intervalo"))
    lista=[]
    for i in range(20,(20+num)+1):
        lista.append(i)
    print (lista)
except ValueError:
        print ("### Ingrese un Número!!###")
