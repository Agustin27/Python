
n1 = raw_input("ingrese un numero")
n2 = raw_input("ingrese un numero")
n3 = raw_input ("ingrese un numero")

x=0
y=0

if n1>n2:
    x=n1
elif n2>n1:
    x=n2

if x>n3:
   x=x
elif n3>n2:
    x=n3
print "El mayor es", x
