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
            for linea in file:
                if IF in linea:
                    contenido += linea
                    print(linea.strip())

        with open('reportefecha.txt', 'w') as file:
            file.write(contenido)


