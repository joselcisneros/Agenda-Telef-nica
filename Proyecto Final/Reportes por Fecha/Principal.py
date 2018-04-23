import Menu
import Busqueda

if __name__ == '__main__':
    Menu.Menu()
    opcion = input('\tEscoja una opción: ')
    if opcion == "1":
        Busqueda.BPF()
    elif opcion == "2":
        print('Aquí va la opciín 2.')
    elif opcion == "3":
        print('Aquí va la opción 3.')
    elif opcion == "4":
        print('Aquí va la opción 4.')
    else:
        print('Gracias.')