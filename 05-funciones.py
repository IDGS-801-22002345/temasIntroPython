import os

def funcion1():
    print("Hola, soy la funcion 1")
    num1=int(input('ingresa el primer numero: '))
    num2=int(input('ingresa el segundo numero: '))
    res=0
    res=num1+num2
    print(f'Resultado de la suma: {res}')

def funcion2():
    print("Hola, soy la funcion restar")
    num1=int(input('ingresa el primer numero: '))
    num2=int(input('ingresa el segundo numero: '))
    res=0
    res=num1-num2
    print(f'Resultado de la resta: {res}')

def funcion3():
    print("Hola, soy la funcion multiplicar")
    num1=int(input('ingresa el primer numero: '))
    num2=int(input('ingresa el segundo numero: '))
    res=0
    res=num1*num2
    print(f'Resultado de la multiplicacion: {res}')

def funcion4():
    print("Hola, soy la funcion multiplicar")
    num1=int(input('ingresa el primer numero: '))
    num2=int(input('ingresa el segundo numero: '))
    res=0
    res=num1/num2
    print(f'Resultado de la divicion: {res}')

def run():
    while True:
     print('1.- Suma')
     print('2.- Restar')
     print('3.- Multiplicar')
     print('4.- Divicion')
     print('5.- Salir')
     op=int(input('Opcion: '))
   
     if op==1:
        funcion1()
     if op==2:
        funcion2()
     if op==3:
        funcion3()
     if op==4:
        funcion4()
     if op==5:
        break
    

# run()

if __name__ == "__main__":
     run()