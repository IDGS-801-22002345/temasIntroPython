range(20)
x=range(10,20)#Empiza en 10
x=range(1,20,2) #haciendo incrementos en 2 en 2


num1=int(input('Ingresa el numero para la tabla: '))
res=0
for i in range(1,11):
  res=num1*i
  print(f'{num1} x {i}= {res}')

print('Fin')

