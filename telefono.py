import re
import os

def buscar (self):
    agenda = open('C:\\Users\\TECNOLOGIA\\Downloads\\hola\\Prueba\\agenda.txt', 'r')
    for linea in agenda.readlines():
        lista = linea.strip().split(", ")
        if num in lista[0]:
            return lista[1]
    agenda.close()

def agregar (self):
    agenda = open('C:\\Users\\TECNOLOGIA\\Downloads\\hola\\Prueba\\agenda.txt', 'a+')
    nombre = input("Introduzca el nombre: ")
    agenda.write('\n' + num + ', '+ nombre)
    print ("Agregado.")
    agenda.close()


if __name__ in '__main__':
    num = input("Introduzca el número: ")
    if buscar(num) != None:
        os.system("cls")
        print ("Llamando a", buscar(num) + '.')
    else:
        pre = input("¿Desea agregar este número? Y/N ")
        if pre == 'Y':
            agregar (num)
            os.system("cls")
            re = input("¿Desea llamar a este número? Y/N: ")
            if re == "Y":
                os.system("cls")
                print ("Llamando a", buscar(num) + '.')
        else:
            os.system("cls")
            print ("Gracias por usar el programa.")