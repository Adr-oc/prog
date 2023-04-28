# Adrian Alejandro Orantes Cameros
# Carne: 23739
# Ejercicio #04 - Algortimos y Programacion basica


# Importar todas las funciones del archivo modules.py
from modules import *

# Declaracion de variables
directory = "Temario D.csv"
temp_content = []

# Menu principal
while True:
    clean_screen()
    options = ['Leer el archivo con los datos actualmente guardados.',
               'Mostrar todos los elementos dentro del archivo en consola.',
               'Agregar un nuevo registro con todos los valores en cada columna.',
               'Modificar el valor de la columna "Seguidores".',
               'Modificar el valor de la columna "Engagement Rate".',
               'Modificar el valor de la columna "Frecuencia".',
               'Imprimir reportes en consola.',
               'Salir']

    # Imprimir el menu principal
    print(Fore.BLUE+'------------MENU------------')
    print(Fore.MAGENTA+'Seleccione una opcion: \nRecomendacion: antes y despues de cualquier opcion utilice la 1. '+Fore.WHITE)
    for i in range(len(options)):
        print(f'{Fore.GREEN}{i + 1}. {Fore.WHITE}{options[i]}')

    opt = input(Fore.YELLOW+'opcion: '+Fore.GREEN)
    Fore.WHITE

    # Validar la opcion seleccionada
    clean_screen()
    match opt:

        case '1':
            # Leer el archivo con los datos actualmente guardados.
            print(Fore.WHITE+'Leyendo el archivo...')
            temp_content = leer_archivo(
                directory, 'Archivo leido correctamente.')

        case '2':
            # Mostrar todos los elementos dentro del archivo en consola.
            if temp_content == 0 or temp_content == []:
                print(
                    Fore.RED+'No se ha leido ningun archivo para mostrar los elementos.')
                input(Fore.WHITE+'Presione enter para continuar...')
            else:

                mostrar_elementos(temp_content)

        case '3':
            # Agregar un nuevo registro con todos los valores en cada columna.
            if temp_content == 0 or temp_content == []:
                print(
                    Fore.RED+'No se ha leido ningun archivo para agregar un nuevo registro.')
                input(Fore.WHITE+'Presione enter para continuar...')
            else:
                # Solicitar los datos para agregar un nuevo registro
                registro = solicitud_datos_para_agregar()

                # Agregar el nuevo registro a la lista
                temp_content = agregar_registro(directory, registro)
        case '4':
            modificar_seguidores(directory, temp_content)

        case '5':
            modificar_engagement_rate(directory, temp_content)

        case '6':
            modificar_frecuencia(directory, temp_content)

        case '7': pass
        case '8': break
