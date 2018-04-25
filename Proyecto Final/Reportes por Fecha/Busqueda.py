def BPF():
    while True:
        total = 0
        os.system('cls')
        print("----------------------------------")
        print("    Sistema de Punto de Ventas    ")
        print("    REPORTE DE VENTAS POR FECHA")
        print("----------------------------------")
        print(" ")
        while True:
            fecha = (input("Ingresa la fecha de búsqueda: "))
            try:
                f = open('ventas.txt', 'r')
            except FileExistsError:
                msn = (input("ERROR: no existe el archivo de ventas"))
                break

            if (fecha == 0):
                return

            for linea in f.readlines():
                linea = linea.split(',')
                if (linea[0] == '2' and linea[7] == fecha):
                    total = float(linea[4]) + total
            break
        msn = (input("Total en ventas por fecha: " + str(total) + "$"))
