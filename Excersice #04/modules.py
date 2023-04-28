# importamos las librerias, os para limpiar la pantalla , csv para leer el archivo y colorama para darle color a la consola
import os
import csv
from colorama import Fore


# funcion para limpiar la pantalla
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# funcion para leer el archivo
def leer_archivo(directory, text):
    with open(directory, mode='r', newline='') as file:
        reader = csv.reader(file)
        temp_content = list(reader)

    print(Fore.GREEN+text+Fore.GREEN)
    input(Fore.WHITE+'Presione enter para continuar...')
    return temp_content


def mostrar_elementos(temp_content):
    print('Mostrando todos los elementos...')
    for i in range(len(temp_content)):
        for j in range(len(temp_content[i])):
            print(Fore.WHITE+temp_content[i][j])
        print(Fore.GREEN+'---------------------------')
    input('Presione enter para continuar...')


# funcion para agregar un nuevo registro
def solicitud_datos_para_agregar():
    print(Fore.WHITE+'Solicitando datos para agregar un nuevo registro...')
    user = str(input(Fore.WHITE+'Ingrese el nombre del usuario: '+Fore.GREEN+"@"))
    user = '@'+user.lower()
    # verificar que la plataforma sea valida
    platforms = ['Instagram', 'YouTube', 'Twitter', 'TikTok']
    platform = input(
        Fore.WHITE+'Ingrese la plataforma (Intagram, YouTube, Twitter, TikTok): '+Fore.GREEN)
    while platform not in platforms:
        print(Fore.RED + 'La plataforma ingresada no es valida.'+Fore.WHITE)
        platform = input(
            Fore.WHITE+'Ingrese la plataforma (Intagram, YouTube, Twitter, TikTok): '+Fore.GREEN)

    # verificar que el numero de seguidores sea mayor a 0 y que sea un numero entero
    followers = int(
        input(Fore.WHITE+'Ingrese la cantidad de seguidores: '+Fore.GREEN))
    while followers < 0 or type(followers) != int:
        print(Fore.RED+'La cantidad de seguidores ingresada no es valida.'+Fore.WHITE)
        followers = int(
            input(Fore.WHITE+'Ingrese la cantidad de seguidores: '+Fore.GREEN))

    # verificar que el engagement rate sea mayor a 0 y sea flotante
    engagement_rate = float(
        input(Fore.WHITE+'Ingrese el engagement rate: '+Fore.GREEN))
    while engagement_rate < 0 or type(engagement_rate) != float:
        print(Fore.RED+'El engagement rate ingresado no es valido.'+Fore.WHITE)
        engagement_rate = float(
            input(Fore.WHITE+'Ingrese el engagement rate: '+Fore.GREEN))

    category = str(input(Fore.WHITE+'Ingrese la categoria: '+Fore.GREEN))
    country = str(input(Fore.WHITE+'Ingrese el pais: '+Fore.GREEN))

    # verificar que la frecuencia sea valida
    frecuency = str(
        input(Fore.WHITE+'Ingrese la frecuencia (diaria, semanal, mensual): '+Fore.GREEN))
    while frecuency != 'diaria' and frecuency != 'semanal' and frecuency != 'mensual':
        print(Fore.RED+'La frecuencia ingresada no es valida.'+Fore.WHITE)
        frecuency = str(
            input(Fore.WHITE+'Ingrese la frecuencia (diaria, semanal, mensual): '+Fore.GREEN))

    registro = [user, platform, followers,
                engagement_rate, category, country, frecuency]
    return registro


# funcion para agregar un nuevo registro
def agregar_registro(directory, registro):
    print('Agregando registro...')
    print(registro)
    with open(directory, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(registro)

    print(Fore.GREEN+'Registro agregado correctamente.')
    input(Fore.WHITE+'Presione enter para continuar...')


# funcion para modificar el valor de la columna "Seguidores"
def modificar_seguidores(directory, temp_content):
    if len(temp_content) == 0:
        print(Fore.RED+'No hay registros para modificar.'+Fore.WHITE)
        input(Fore.WHITE+'Presione enter para continuar...')
    else:
        print('Modificando el valor de la columna "Seguidores"...')
        user = str(input(
            Fore.WHITE+'Ingrese el nombre del usuario al que desea modificar los seguidores: '+Fore.GREEN+"@"))
        user = '@'+user.lower()
        for i in range(len(temp_content)):
            if temp_content[i][0] == user:
                followers = int(
                    input(Fore.WHITE + 'Ingrese la cantidad de seguidores nueva para: '+user + ' :' + Fore.GREEN))
                while followers < 0 or type(followers) != int:
                    print(
                        Fore.RED+'La cantidad de seguidores ingresada no es valida.'+Fore.WHITE)
                    followers = int(
                        input(Fore.WHITE+'Ingrese la cantidad de seguidores: '+Fore.GREEN))

                temp_content[i][2] = followers
                save_file(directory, temp_content)
                leer_archivo(
                    directory, 'Seguidores modificados correctamente.')
                no_user_found = False
                break
            else:
                no_user_found = True

        if no_user_found:
            print(Fore.RED+'No se encontro el usuario ingresado.'+Fore.WHITE)
            input(Fore.WHITE+'Presione enter para continuar...')


# funcion para modificar el valor de la columna "Engagement Rate"
def modificar_engagement_rate(directory, temp_content):
    if len(temp_content) == 0:
        print(Fore.RED+'No hay registros para modificar.'+Fore.WHITE)
        input(Fore.WHITE+'Presione enter para continuar...')
    else:
        print('Modificando el valor de la columna "Engagement Rate"...')
        user = str(input(
            Fore.WHITE+'Ingrese el nombre del usuario al que desea modificar el engagement rate: '+Fore.GREEN+"@"))
        user = '@'+user.lower()
        for i in range(len(temp_content)):
            if temp_content[i][0] == user:
                engagement_rate = float(
                    input(Fore.WHITE + 'Ingrese el engagement rate nuevo para: '+user + ' :' + Fore.GREEN))
                while engagement_rate < 0 or type(engagement_rate) != float:
                    print(
                        Fore.RED+'El engagement rate ingresado no es valido.'+Fore.WHITE)
                    engagement_rate = float(
                        input(Fore.WHITE+'Ingrese el engagement rate: '+Fore.GREEN))

                temp_content[i][3] = engagement_rate
                save_file(directory, temp_content)
                leer_archivo(
                    directory, 'Engagement rate modificado correctamente.')
                no_user_found = False
                break
            else:
                no_user_found = True

        if no_user_found:
            print(Fore.RED+'No se encontro el usuario ingresado.'+Fore.WHITE)
            input(Fore.WHITE+'Presione enter para continuar...')

# funcion para modificar el valor de la columna "Frecuencia"


def modificar_frecuencia(directory, temp_content):
    if len(temp_content) == 0:
        print(Fore.RED+'No hay registros para modificar.'+Fore.WHITE)
        input(Fore.WHITE+'Presione enter para continuar...')
    else:
        print('Modificando el valor de la columna "Frecuencia"...')
        user = str(input(
            Fore.WHITE+'Ingrese el nombre del usuario al que desea modificar la frecuencia: '+Fore.GREEN+"@"))
        user = '@'+user.lower()
        for i in range(len(temp_content)):
            if temp_content[i][0] == user:
                frecuency = str(
                    input(Fore.WHITE+'Ingrese la frecuencia nueva para: '+user + ' :' + Fore.GREEN))
                while frecuency != 'diaria' and frecuency != 'semanal' and frecuency != 'mensual':
                    print(Fore.RED+'La frecuencia ingresada no es valida.'+Fore.WHITE)
                    frecuency = str(
                        input(Fore.WHITE+'Ingrese la frecuencia (diaria, semanal, mensual): '+Fore.GREEN))

                temp_content[i][6] = frecuency
                save_file(directory, temp_content)
                leer_archivo(
                    directory, 'Frecuencia modificada correctamente.')
                no_user_found = False
                break
            else:
                no_user_found = True
        if no_user_found:
            print(Fore.RED+'No se encontro el usuario ingresado.'+Fore.WHITE)
            input(Fore.WHITE+'Presione enter para continuar...')

# funcion para imprimir reportes


def imprimir_reportes():
    print('Imprimiendo reportes...')


def save_file(directory, registro):
    with open(directory, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(registro)
