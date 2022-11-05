def agregarCiclista():
    ciclista = {}
    ciclista['nombre'] = input("Digite el nombre: ")
    ciclista['edad'] = input("Digite la edad: ")
    ciclista['pais'] = input("Digite el pais: ")
    ciclista['equipo'] = input("Digite el equipo: ")
    ciclista['tiempo'] = int(input("Digite el tiempo del ciclista: "))

    print('Ciclista guardado exitosamente')

    return ciclista
