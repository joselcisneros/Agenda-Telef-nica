def BPF():
    import os.path
    verificador = os.path.isfile('reporte.txt')
    if verificador == False:
        print('El archivo que contiene los reportes no existía y fue creado.')
        with open('reporte.txt', 'w') as file:
            file.close()
    elif os.stat('reporte.txt').st_size == 0:
        print('Este archivo no contiene información.')
    else:
        with open('reporte.txt') as file:
            contenido = ''
            IF = input('Introduzca la fecha con el siguiente formato (aaaa-mm-dd): ')
            for linea in file.readlines():
                lista = linea.strip().split(', ')
                if IF in lista[0]:
                    contenido += linea
                    print(linea.strip())
            if IF != lista[0]:
                print('El dato introducido no es válido o no existe.')

        with open('reportefecha.txt', 'w') as file:
            file.write(contenido)
