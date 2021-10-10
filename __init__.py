# -*- coding: utf-8 -*-
# !/usr/bin/python

import numpy as np
import numexpr as ne

from sys import exit as sysexit
from os import remove as osremove
from getpass import getuser
from time import sleep, time
from vector_binario import vector_binario
from obtain_data import obtain_data
from welcome import welcome

username = getuser()

welcome(username)

while True:
    try:
        print('\n')
        contenedor = float(input('-Introduce la capacidad con la que agrupar (MB): '))
        if contenedor <= 0:
            print(u'\n # Error: ¡¡¡ debe ser un numero positivo y mayor que cero !!!  #\n')
        else:
            break
    except:
        print(u'\n #  Error: ¡¡¡recuerda que debe ser un numero!!!  #\n')

#Introducir la dirección de la elemento con los elementos a agrupar
while True:
#    try:
    print(u'-Introduce la dirección entre comillas o arrastra la carpeta hasta aquí:')
    direccion = input()
    if '"' in direccion or "'" in direccion:
        direccion = direccion[1:-1]
    donde_abrir = direccion + '/grupos.txt'
    fo = open(donde_abrir, 'w+')  # donde se escribirán los grupos
    break
#    except:
    print(u'\n#  Error: Dirección no válida # -> si el error persiste ver la ayuda  #\n')

##escribimos el título del programa en el txt
fo.write('\n')
fo.write('   ******  **   **       ******   *****      **      *****   **  **\n')
fo.write('   **      **   **       **       **  **    ** *    **       ** ** \n')
fo.write('   ****    **   **       ****     ****     ******   **       ****  \n')
fo.write('   **      **   **       **       **       **  **   **       ** ** \n')
fo.write('   **      **   ******   ******   **       **  **    *****   **  **  : by J-one\n\n\n')

##apuntamos datos en el fichero grupos.txt

frase = '      La capacidad escogida de los grupos es de ' + str(contenedor) + ' MB'

fo.write('  ' + (len(frase) + 4) * '*' + '\n')
fo.write(frase + '\n')
fo.write('  ' + (len(frase) + 4) * '*' + 3 * '\n')

##---------------------------------------------------------------------------------------
# Obtenemos la lista de los elementos y sus tamaños
##---------------------------------------------------------------------------------------

lista_elementos, sizes = obtain_data(direccion)

##---------------------------------------------------------------------------------------
# Comprobamos que ninguna elemento sea demasiado grande
##---------------------------------------------------------------------------------------

eleccion = ''
lista_elementos_borrar = []

for i in range(len(lista_elementos)):
    if sizes[i] > contenedor:
        elemento_grande = lista_elementos[sizes.index(sizes[i])]

        # mensaje de error-------------------------------------------------------------
        frase1 = '## El elemento "' + \
        elemento_grande + '" es demasiado grande.'
        frase2 = '## Ocupa ' + str(sizes[i]) + '(MB);' + 'es mayor de ' + str(contenedor) + '(MB).'

        if len(frase1) > len(frase2):
            frase2 += (len(frase1) - len(frase2)) * ' ' + '##'
            frase1 += '##'
        elif len(frase1) < len(frase2):
            frase1 += (len(frase2) - len(frase1)) * ' ' + '##'
            frase2 += '##'
        else:
            frase1 += ' ##'
            frase2 += ' ##'

        print('\n')
        print(max(len(frase1), len(frase2)) * '#')
        print(frase1)
        print(frase2)
        print(max(len(frase1), len(frase2)) * '#' + '\n')
        # --------------------------------------------------------------mensaje de error

        if eleccion != 'i':

            while True:
                eleccion = input(' Introduzca:\n -Para continuar e ignorarla "c":\n '
                '-Para ignorar todas "i":\n -Para salir "s":\n')
                if eleccion == 's':
                    fo.close()
                    osremove(donde_abrir)
                    print('\n')
                    print('  #########################################')
                    print('  ###             Saliendo              ###')
                    print('  #########################################\n')
                    sleep(1.5)
                    sysexit()
                elif (eleccion == 'c') or (eleccion == 'i'):
                    lista_elementos_borrar += [elemento_grande]
                    break
                else:
                    print(' *** siga las indicaciones ***\n')
        else:
            lista_elementos_borrar += [elemento_grande]

if len(lista_elementos_borrar) == 1:
    fo.write('  ' + str(lista_elementos_borrar) + ' es demasiado grande.\n\n\n')
elif len(lista_elementos_borrar) > 1:
    fo.write('  ' + str(lista_elementos_borrar) + ' son demasiado grandes.\n\n\n')

# eliminamos de los tamaños y de la lista de elementos que sobrepasan el espaico asignado

for i in lista_elementos_borrar:
    sizes.remove(sizes[lista_elementos.index(i)])
    lista_elementos.remove(i)

#-------------------------------------------------------------------------------------------

##----------------------------------------------------------------------------------------
# obtenemos los grupos de elementos que caben en una cierta cantidad
##----------------------------------------------------------------------------------------

sublista_elementos = lista_elementos  # lista auxiliar de elementos
subsizes = sizes  # lista auxiliar de tamaños de elementos

print('\n')
print(' Los elementos a agrupar son : ' + '(' + str(len(sublista_elementos)) + ')')
print(' ' + str(sublista_elementos) + '\n\n')

n_grupo = 0  # numero del grupo de elementos

print(' Ocupan : ' + '(' + str(len(sizes)) + ')')
print(' ' + str(sizes) + '\n\n')

input('  ...presiona ENTER para continuar:\n')

print('\n Calculando...\n')
print(' Espere por favor.\n Esto puede tardar un rato...\n\n')

try:
    while ne.evaluate('sum(subsizes)') > contenedor:

        n_grupo += 1

        total = len(sublista_elementos)  # número total de elementos

    #----------------------------------------------------------------------------------------
    # Realizamos todas las combinaciones posibles
    #----------------------------------------------------------------------------------------

        suma = 0

        for i in range(len(subsizes)):
            suma += sorted(subsizes)[i]
            if suma > contenedor:
                nmax = i  # los máximos elementos que cabrían (uno menos que el de la condición)
                break

        start_time = time()  # ttttttttttttt  medimos el tiempo de ejecucion tttttttttttttt

        for i in range(1, 2 ** total):
            vector_bin_ = vector_binario(i, len(subsizes))
            A_ = np.zeros(len(subsizes))

            for j in range(len(vector_bin_)):
                if ne.evaluate('sum(vector_bin_)') > nmax:
                    break
                A_[j] = vector_bin_[j] * subsizes[j]  # todas las combinaciones posibles

            #sustituyo el valor por el actual si se acerca más al valor del contenedor sin pasarse
            try:
                resto_ = contenedor - ne.evaluate('sum(A_)')
                if i == 1:
                    A = A_  # será el primero
                    vector_bin = vector_bin_
                    resto = contenedor - ne.evaluate('sum(A)')  # nuevo resto
                elif (resto_ < resto) and (resto_ >= 0):
                    A = A_  # sustituyo el actual por el anterior
                    vector_bin = vector_bin_
                    resto = contenedor - ne.evaluate('sum(A)')  # nuevo resto
            except:
                print('error')

     #----------------------------------------------------------------------------------------

     # para poder operar con los nombres de los elementos y tamaños los transformamos en array

        elementos = np.array(sublista_elementos)
        sizes2 = np.array(subsizes)

     # vemos cuales son los elementos ya agrupados---------------------------------------------

        elementos_agrupados = []
        subsizes_agrupados = []

        for i in range(len(vector_bin)):
            if vector_bin[i] == 1:
                elementos_agrupados += [elementos[i]]  # elementos ya agrupados
                subsizes_agrupados += [sizes2[i]]  # espacios de las elementos agrupados
                sublista_elementos.remove(elementos[i])  # quitamos el elemento agrupado del total
                subsizes.remove(sizes2[i])  # quitamos los tamaños del total

     ##----------------------------------------------------------------------------------------
     # Escribimos en el archivos que nos indicará los grupos de los elementos ("grupos.txt")
     ##----------------------------------------------------------------------------------------

        titulo_grupo = '    # Grupo: ' + str(n_grupo) + ' #'

        fo.write(titulo_grupo)
        fo.write('  ' + str(elementos_agrupados) + '\n')

        resto_porcentaje = resto * 100 / contenedor
        resto_que_queda = '  Espacio desaprovechado : ' + str(resto) + ' MB = '\
         + str(resto_porcentaje) + ' %'
        fo.write(resto_que_queda + 3 * '\n')

        #vamos haciendo el seguimiento por pantalla

        print(len(titulo_grupo) * '--')
        print(titulo_grupo)
        print(len(titulo_grupo) * '--' + '\n')
        print(' Elementos_agrupados: (' + str(len(elementos_agrupados)) + ')')
        print(' ' + str(elementos_agrupados) + '\n')

        print(' Ocupan: ')
        print(str(subsizes_agrupados) + ' MB \n')

        print(' Queda por agrupar: (' + str(len(sublista_elementos)) + ')')
        print(' ' + str(sublista_elementos) + '\n')

        elapsed_time = time() - start_time
        print('\n Transcurridos %0.5f segundos.\n' % elapsed_time)

except:
    print('\n')
    print('##################################################################')
    print('# Error en el procesado de los datos:                            #')
    print('##################################################################')
    print(' ...Compruebe que se cumplen los requisitos.              \n')

    fo.close()
    osremove(donde_abrir)  # borramos el "grupos.txt", ya que ha dado error

    input('Presione ENTER para salir:\n')
    sysexit()

##-------------------------------------------------------------------------------------------
# terminamos el fichero con el grupo de los elementos restantes
##-------------------------------------------------------------------------------------------

n_grupo += 1
elementos_agrupados = sublista_elementos
subsizes_agrupados = subsizes

titulo_grupo = '    # Grupo: ' + str(n_grupo) + ' #'

fo.write(titulo_grupo + '----------------\n')
fo.write('  ' + str(elementos_agrupados) + '\n')

resto = contenedor - sum(subsizes)

resto_que_queda = '  Espacio desaprovechado : ' + str(resto) + ' MB = '\
 + str(resto * 100 / contenedor) + ' %'
fo.write(resto_que_queda + 4 * '\n')

fo.write('  ' + (len(frase) + 4) * '*' + '\n')
fo.write(round((len(frase) - 23) / 2) * ' ' + 'Ha finalizado correctamente   \n')
fo.write('  ' + (len(frase) + 4) * '*' + '\n')

fo.close()

titulo_grupo = ' # Grupo: ' + str(n_grupo) + ' #'

print(len(titulo_grupo) * '--')
print(titulo_grupo)
print(len(titulo_grupo) * '--' + '\n')
print(' Elementos_agrupados: (' + str(len(elementos_agrupados)) + ')')
print(' ' + str(elementos_agrupados) + '\n')

print(' Ocupan: ')
print(str(subsizes_agrupados) + ' MB' + '\n\n')

print('  #########################################')
print('  ###    Ha finalizado correctamente    ###')
print('  #########################################')
print('                                   by J-one')

input('Presione ENTER para SALIR\n')
