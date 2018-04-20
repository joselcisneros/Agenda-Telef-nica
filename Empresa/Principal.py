import Menu
import Opciones


if __name__ == '__main__':
    Menu.Menu_Principal()
    opcion = input('\t Escoja una opción: ')
    if opcion == "1":
        Opciones.Opcion_Agregar()
    elif opcion == "2":
        Opciones.Opcion_Modificar()
    elif opcion == "3":
        Opciones.Opcion_Eliminar()
    else:
        print ('Gracias.')