"""
2. Codificar un programa en Python utilizando funciones lamba que
permita: recibir 2 números y devolver
1 → si el primer número es mayor que el segundo
-1→ si el primer número es menor que el segundo
Después una segunda función debe recibir el 1 o el -1 retornado por
la función 1 y mostrar un mensaje
Si recibe 1 → Debe indicar que el primer número es mayor
Si recibe -1 → Debe indicar que el segundo número es mayor
Recomendaciones: Utilizar operador ternario +1
"""

from ast import Lambda


numeroUno = int(input("Digite el primer numero: "))
numeroDos = int(input("Digite el segundo numero numero: "))

mayor = lambda numeroUno, numeroDos : (1 if numeroUno > numeroDos else -1)

Mostrar = lambda numero : "El primer número es mayor" if numero == 1 else "El segundo número es mayor"

print(Mostrar(mayor(numeroUno,numeroDos)))