from funciones.cuenta import Cuenta
from funciones.cliente import Cliente

cliente1 = Cliente()
cliente1.nombre = 'Maria Fernanda'
cliente1.apellido = 'Molina Fernandez'
cliente1.cedula = '1000205612'
cliente1.ciudad = 'Medellín'

cuenta1 = Cuenta()
cuenta1.numeroCuenta = '123456'
cuenta1.saldo = '10000'

opcion  = 10


print("Menu")
print("1.Consultar Saldo")
print("2. Ingresar ")
print("3.Retirar")
print("0. Salir")

while opcion!=0:
    
    opcion = int(input("Digita una opcion: "))
    if (opcion == 1):
         print(f"El saldo es:  $" + (cuenta1.saldo) )
         
    elif (opcion ==2):
         dinero = int(input("Digita el monto: "))
         suma = dinero + int(cuenta1.saldo)
         cuenta1.saldo = suma
         print(f"El saldo es: ${suma}")
    
    elif( opcion ==3):
         dinero2 = int(input("Digita el monto a retirar: "))
         resta =int(cuenta1.saldo) - dinero2 
         cuenta1.saldo =  resta
         print(f"El saldo es: ${resta}")

    
    elif (opcion ==0):
         print()

        
    elif (opcion ==0):
        break
    else:
        print("Opción no válida")

else:
    print("Transaccion finalizada")