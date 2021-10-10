# -*- coding: utf-8 -*-
# !/usr/bin/python


def welcome(username):

    from time import sleep
    from sys import exit as sysexit
    from os import name as osname
    from os import system as ossystem

    ossystem('cls' if osname == 'nt' else 'clear')

    print('\n')
    print('   ******  **   **       ******   *****      **      *****   **  **')
    print('   **      **   **       **       **  **    ** *    **       ** ** ')
    print('   ****    **   **       ****     ****     ******   **       ****  ')
    print('   **      **   **       **       **       **  **   **       ** ** ')
    print('   **      **   ******   ******   **       **  **    *****   **  **  : by J-one\n')

    print(('Bienvenid@ ' + str(username) + ';\n'))

    while True:
        try:
            eleccion = input(' Introduzca:\n -Para comenzar "c":\n -Para ayuda "a":\n'
            ' -Para salir "s":\n')
            print('\n')

            if (eleccion == 's'):
                break

            elif (eleccion == 'a'):
                print('# OBJETIVO: #\n-------------')
                print(u'El objetivo de este programa es agrupar carpetas según cierto tamaño'
                ' asignado.')
                print(u'El criterio para agrupar es el de que no sobrepasen el espacio'
                u' determinado, sobrando lo menos posible, y consiguiendo elmenor número de grupos'
                '.\n')

                input('Presiona ENTER...\n')

                print('# REQUISITOS PREVIOS: #\n-----------------------')
                print(u'-La carpeta madre que contiene las carpetas a agrupar debe tener '
                u'únicamente carpetas para que el empaquetamiento fucnione; excepto si está '
                u'presente el fichero "grupos.txt" creado por FILEPACK anteriormente '
                u'; éste se reemplazará y no es problema.')
                print(u'-Se ignorarán:')
                print(u' * Lo que no sea carpeta')
                print(u' * Las carpetas ocultas')
                print(u'-En el caso de haber alguna carpeta mayor que el espacio reservado'
                u' para hacer los grupos, el programa lo avisa. Se podrá escoger entre seguir '
                u', en cuyo caso se ignora; o se sale para volver a iniciar el programa y '
                u'rectificar la capacidad de los grupos.')
                print(u'-El tiempo del proceso depende principalmente de la cantidad de carpetas'
                u' a agrupar. En caso de no poder trabajar con tal cantidad el programa'
                u' lo avisaría; el resto es esperar.\n')
                print(u'-El limitante puede ser el numero de carpetas a agrupar, que depende de '
                u'de la potencia del ordenador que se esté utilizando.\n')

                input('Presiona ENTER...\n')

                print('\n')
                print('# INSTRUCCIONES: #\n------------------')
                print(u' *Se pide la capacidad a asignar a los grupos de carpetas.')
                print(u' *La dirección a especificar es la "carpeta madre" que contiene las '
                'carpetas que se desean agrupar.')
                print(u' *Cuando el programa haya finalizado se habrá creado un archivo '
                u'"grupos.txt" con el contenido de los grupos formados en la carpeta madre.\n')

                print('\n')
                print(' Espero que haya sido de ayuda.\n J-one')
                print('\n')

                print(u' Presiona ENTER para volver al MENÚ PRINCIPAL.')
                input()
                print('\n')

            elif (eleccion == 'c'):
                print('\n')
                print('  #########################################')
                print('  ###             Comenzamos            ###')
                print('  #########################################')
                print('\n')
                break

            else:
                print('********* Sigue las indicaciones. *************\n')
                print('\n')

        except:
            print('********* Sigue las indicaciones. *************\n')
            print('\n')

    if (eleccion == 's'):
        print('\n')
        print('  #########################################')
        print('  ###             Saliendo              ###')
        print('  #########################################\n')

        sleep(1.5)
        sysexit()

    return(eleccion)
