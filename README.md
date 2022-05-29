# Filepack
 Bin packing for files

Aviso: Ésta es una versión beta para uso doméstico. Cae toda la responsabilidad sobre el que utiliza el programa de los posibles efectos.
Tras ejecutar se le guiará durante todo el proceso.
Lea y siga las instrucciones con atención.

-------------------------------------------------------------------------------------------
 Para ejecutar el programa:
-------------------------------------------------------------------------------------------

*En Windows:

  Ejecutas exec_windows.bat. Si no funciona, dar permisos de administrador.

*En Linux:

  En propiedades dale permiso de ejecución.

  Ejecutas exec_linux.sh en un terminal. Te pedirá permisos de superusuario.

-------------------------------------------------------------------------------------------
 Comentarios:
-------------------------------------------------------------------------------------------

 Este programa necesita ciertos privilegios simplemente porque tiene que crear archivos en
la carpeta con la que trabaja, para finalmente dejarte un .txt llamado "grupos.txt".
En éste estarán organizados los grupos con las subcarpetas, sus espacios correspondientes y
el resto que queda respecto al tamaño máximo que se le ha asignado a los contenedores ficticios.

 El programa explica todo durante el proceso y da las recomendaciones pertinentes.

 Aunque ya se avisa al principio del proceso, se menciona que este programa ha sido desarrollado
en python, por lo que el usuario deberá tenerlo previamente instalado en su ordenador.

 Cualquier fallo, sugerencia, o duda no duden en comunicármelo e intentaremos darle solución; 
 tengan en cuenta que es una versión beta.

 Un cordial saludo


------------------------------------------------------------------------------------------------
Se adjunta una copia de la "ayuda" del programa, la cual encontrará también al ejecutarlo, antes
de que realice nada y con opción de cancelar antes de que empiece ha hacer nada con los ficheros.
------------------------------------------------------------------------------------------------


# OBJETIVO: #

.El objetivo de este programa es el de agrupar en una lista una serie de
 carpetas contenidas a su vez en una "carpeta madre".
.El criterio para agruparlas será el de que no sobrepasen un espacio
determinado por el usuario, hasta que no queden carpetas.


# REQUISITOS PREVIOS: #

-En el caso de haber alguna carpeta mayor que el espacio reservado para hacer los grupos,
 el programa lo avisará, pero se deberá prescindir de dicha carpeta para que el programa 
pueda funcionar.

-El tiempo del proceso depende principalmente de la cantidad de carpetas y de archivos que contengan.

-En el caso de introducir acentos en la dirección a trabajar se han acusado errores en Windows.

# INSTRUCCIONEs: #

*Se pide la capacidad a asignar a los grupos de carpetas.
*La direccion a especificar es la "carpeta madre" que contiene las carpetas que se desean agrupar.
*Cuando el programa haya finalizado habra creado un archivo "grupos.txt" con el contenido de los grupos formados con las carpetas.

Espero que te sea de utilidad.
