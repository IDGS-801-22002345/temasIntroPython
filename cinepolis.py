class Cinepolis:
     def __init__(self):
         self.nombre=""
         self.numPersonas=0
         self.opMenu=0
         self.opPago= 0
         self.numBoletos= 0
         self.maxBoletos = 0
         self.pago = 0
         self.boletoIndivudal= 12
         self.totalPagar = 0
         self.totalVenta = 0
         self.descuento= 0
         self.venta = []
         self.ticket=""
    
     def descuentoPorBoleto(self):
         self.descuento=0
         self.totalPagar= self.numBoletos * self.boletoIndivudal
         if self.numBoletos > 5:
             self.descuento = self.totalPagar * 0.15
         if self.numBoletos >= 3 and self.numBoletos <= 5:
             self.descuento = self.totalPagar * 0.10
         self.totalPagar -= self.descuento

     def guardarVenta(self):
         self.totalVenta = 0
         self.ticket=open("Ticket.txt","w")
         self.ticket.write("=====================================\n")
         self.ticket.write("          Ticket Cinepolis           \n")
         self.ticket.write("=====================================\n")
         numCompra = 1
         for venta in self.venta:
            nombre, total, boletos = venta
            self.totalVenta += total 
            self.ticket.write(f"-----------------Venta {numCompra}--------------------\n") 
            self.ticket.write(f"Cliente: {nombre}\n")
            self.ticket.write(f"Boletos: {boletos}\n")
            self.ticket.write(f"Total de la compra: ${total}\n")
            self.ticket.write("-------------------------------------\n")
            numCompra += 1

         self.ticket.write("\n=====================================\n")
         self.ticket.write(f"Total de la venta: ${self.totalVenta}\n")
         self.ticket.write("=====================================\n")
         self.ticket.close()  

     def imprimirVenta(self):
        self.guardarVenta()
        texto = open("Ticket.txt", "r")
        lectura = texto.readlines()  
        texto.close() 
        for linea in lectura:
                print(linea)

        self.venta = []

     def capturarDatos(self):
         self.nombre=input('Ingrese su nombre completo: ')
         self.numPersonas=int(input('Ingrese el numero de personas: '))
         self.numBoletos = int(input("Número de boletos a comprar: "))
         
         self.maxBoletos = self.numPersonas * 7
         
         while self.numBoletos > self.maxBoletos:
            print(f"No puedes comprar más de {self.maxBoletos} boletos.")
            
            while True:
                print("\n¿Qué deseas modificar?")
                print("1.- Modificar número de boletos")
                print("2.- Modificar número de personas")
                opcion = int(input("Elige una opción: "))
                
                if opcion == 1:
                    self.numBoletos = int(input("Ingrese un nuevo número de boletos: "))
                    if self.numBoletos <= self.maxBoletos:
                        break
                    else:
                        print(f"No puedes comprar más de {self.maxBoletos} boletos.")
                if opcion == 2:
                    self.numPersonas = int(input('Ingrese el número de personas: ')) 
                    self.maxBoletos = self.numPersonas * 7
                    if self.numBoletos <= self.maxBoletos:
                        break
                else:
                    print("Opción inválida, intenta de nuevo.")
        
         self.descuentoPorBoleto()
         print('\n-----------------------------------')
         print("Selecciona tu método de pago")
         print("1.- Efectivo")
         print("2.- Tarjeta CINECO (10% de descuento adicional)")
         print('-----------------------------------')


         while True:
            self.opPago = int(input("Opción: "))
            print('-----------------------------------\n')


            if self.opPago == 1:
                print(f"Total a pagar: ${self.totalPagar}")
                self.venta.append((self.nombre,self.totalPagar, self.numBoletos))
                self.guardarVenta()
                break  
            elif self.opPago == 2:
                self.totalPagar *= 0.90  
                print(f"Total con descuento por tarjeta CINECO: ${self.totalPagar}")
                self.venta.append((self.nombre,self.totalPagar,self.numBoletos))
                self.guardarVenta()
                break
            else:
                print("Opción inválida, intenta de nuevo.")
        
         
            

    
     def menu(self):
       texto = open("Ticket.txt", "w")
       texto.close() 
       while True:
        print('\n-----------------------------------')
        print('1.- Comprar boletos')
        print('2.- Terminar')
        self.opMenu=int(input('Opcion: '))
        print('-----------------------------------')

    
        if self.opMenu==1:
           self.capturarDatos()
        if self.opMenu==2:
            self.imprimirVenta()
            break
       

def main(): 
     obj=Cinepolis()
     obj.menu()

if __name__ == "__main__":
     main()
