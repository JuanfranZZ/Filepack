# -*- coding: utf-8 -*-
# !/usr/bin/python


def obtain_data(direccion):

    import os

    from sys import exit as sysexit

    try:
        donde_abrir = direccion + '/carpetas.txt'  # para tener la direccion donde crear el fichero
        fo = open(donde_abrir, 'w+')  # donde se escribirán los tamaños de cada carpeta
    except:
        print('direccion no valida')
    # definimos una lista con los nombres de las carpetas

    lista_carpetas = os.listdir(direccion)
    lista_carpetas.remove('carpetas.txt')  # para que no tenga en cuenta el archivo creado

    if 'grupos.txt' in lista_carpetas:
        lista_carpetas.remove('grupos.txt')  # para quitar este archivo si ha sido creado

    # quitamos de la lista carpetas ocultas (que empiecen por un punto).
    for i in lista_carpetas:
        letra = list(range(len(i)))
        nombre_carpeta = i
        for j in range(len(i)):
            letra[j] = nombre_carpeta[j]
            if j == 1:
                break
        if letra[0] == '.':
            lista_carpetas.remove(str(nombre_carpeta))

    ##----------------------------------------------------------------------------------------
    # Se irán sumando lo que vale cada fichero dentro de cada carpeta
    ##----------------------------------------------------------------------------------------

    for i in lista_carpetas:
        carpeta = direccion + '/' + str(i)

        tamagnos = 0
        for base, dirs, files in os.walk(carpeta):
        ##-leo el tamaño de todo dentro de cada carpeta y los escribo en 'carpetas.txt'
            size = sum(os.path.getsize(os.path.join(base, name)) for name in files)
            tamagnos += size  # esto es para si hay alguna subcarpeta la sume en el bucle

        tamagnos = str(tamagnos / 1000000.0)  # las paso a MB
        fo.write(tamagnos + '\n')

    fo.close()

    ##--------------------------------------------------------------------------------------
    # obtengo los datos
    ##--------------------------------------------------------------------------------------

    # abro para leer los tamaños de las carpetas
    fo = open(donde_abrir, 'r+')

    sizes = fo.read().strip().split('\n')
    # sizes tiene todos los tamaños de las carpetas

    fo.close()

    os.remove(donde_abrir)  # borro el archivo carpetas.txt, porque ya no hace falta

    #quito los elementos que ocupan 0 -> los ficheros sueltos y las carpetas vacias
    while '0.0' in sizes:
        lista_carpetas.remove(lista_carpetas[sizes.index('0.0')])
        sizes.remove('0.0')

    if (len(lista_carpetas) != len(sizes)):
        print('\n')
        print('##################################################################')
        print(u'# Error en la obtención de los datos:                            #')
        print('##################################################################\n')

        input('... presione ENTER para salir:\n')
        sysexit()

    try:
        for i in range(len(lista_carpetas)):
            sizes[i] = float(sizes[i])  # lo paso todo a 'float' para poder operar con ello
        print('\n   Datos obtenidos correctamente...\n')
    except:
        print('\n')
        print('##################################################################')
        print(u'# Error en la obtención de los datos:                            #')
        print('##################################################################\n')

        input('... presione ENTER para salir:\n')
        sysexit()

    print(u'\n ## No se tienen en cuenta las carpetas vacías ni los archivos sueltos. ##\n')

    return (lista_carpetas, sizes)

    sysexit()
