def obtenerResultados(listaCiclistas):
    ciclistaMenor=listaCiclistas[0]
    
    for ciclista in listaCiclistas:

            if ciclista['tiempo'] < ciclistaMenor['tiempo']:
                ciclistaMenor=ciclista
        

    print(f'El ciclista más rápido es: {ciclistaMenor}')
    