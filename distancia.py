import math
# x1=-4
# x2=2
# y1=-3
# y2=5
class OperasBas:
     def __init__(self):
         self.x1=0
         self.x2=0
         self.y1=0
         self.y2=0
    # declaracion de metodos de clase
     def solucion(self):
          self.res=math.sqrt((math.pow((self.x2 - self.x1),2))+(math.pow((self.y2-self.y1),2)))
          print("El resultado es: {}".format(self.res))
     def pedir(self):
            self.x1=int(input('Ingresa x1: '))
            self.x2=int(input('Ingresa x2: '))
            self.y1=int(input('Ingresa y1: '))
            self.y2=int(input('Ingresa y2: '))

def main():
     obj=OperasBas()
     obj.pedir()
     obj.solucion()

if __name__ == "__main__":
     main()