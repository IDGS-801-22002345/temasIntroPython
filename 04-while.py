# x=0

# while x<10:
#     print(x)
#     x=x+1


# Operacion de multiplicacion de a * b utilizando sumas
# a=3
# b=4
# salida: 3+3+3+3+3=12

num1=int(input('ingresa la base: '))
num2=int(input('ingresa las veces que se va repetir: '))
salida="Salida :"

x=0
res=0
while x<num2:
    res=res+num1
    x=x+1
    salida+=str(num1)+"+"
salida+="="+str(res)

print(salida)