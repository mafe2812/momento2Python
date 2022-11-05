from funciones.menu import menu
from funciones.agregar import agregarCiclista
from funciones.obtener import obtenerResultados


opcion=0
ciclistas=[]

menu()
while opcion != -1:
    opcion=int(input("Digite una opción: "))

    if(opcion==1):
        ciclistas.append(agregarCiclista())
    elif(opcion==2):
        obtenerResultados(ciclistas)
    elif(opcion==0):
        break
    else:
        print("Digite una opcion valida: ")
            
