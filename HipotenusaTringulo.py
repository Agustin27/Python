import math
print ("calcular la hipotenusa de un tri�ngulo rect�ngulo---")
print (" ")

catA = float(input("igrese el valor del cateto A"))
catB = float(input("ingrese el valor del catebo B"))


hipotenusa=(catA**2)+(catB**2)
hipotenusa=math.sqrt(hipotenusa)
hipotenusa=float(hipotenusa)
print ("la hipotenusa es: " , hipotenusa)
