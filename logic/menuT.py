import os
import profesores
import alumnos


def Profes():
    while True:
        print("Que desea realizar?")
        print("1.- ¿Registro de Profesor?")
        print("2.- ¿Obtener el dato de un profesor?")
        print("3.- ¿Actualizar datos del Profesor?")
        print("4.- ¿Eliminar registro de 1 profesor")
        print("5.- Ver Todos los Registros")
        print("6.- Volver al Menu Inicial")
        print("7.- Salir")
        opcion = input("Elegir una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            try:
                if opcion == 1:
                    profesores.registroProfesores()
                if opcion == 2:
                    profesores.obtenerDatoProfesor()
                if opcion == 3:
                    profesores.actualizarDatosProfesor()
                if opcion == 4:
                    profesores.eliminarDatosProfesor()
                if opcion == 5:
                    profesores.mostrarDatosGeneral()
                if opcion == 6:
                    os.system("cls")
                    menuTotal()
                if opcion == 7:
                    os.system("cls")
                    print("Te has desconectado...")
                    exit()
                    break
                if opcion != 7:
                    os.system("cls")
                    print(f"{opcion}: Numero no aceptado.")
            except ValueError:
                print("Error, solo elige la opcion en numeros")
        else:
            os.system("cls")
            print(f"\nERROR!, '{opcion}': No es una opcion corecta. Solo se permiten Digitos.\n")


def Alumnos():
    while True:
        print("Que desea realizar?")
        print("1.- ¿Registro de Alumnos?")
        print("2.- ¿Obtener el dato de un Alumno?")
        print("3.- ¿Actualizar datos del Alumno?")
        print("4.- ¿Eliminar registro de 1 Alumno")
        print("5.- Ver Todos los Registros")
        print("6.- Volver al Menu Inicial")
        print("7.- Salir")
        opcion = input("Elegir una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            try:
                if opcion == 1:
                    alumnos.registroAlumnos()
                if opcion == 2:
                    alumnos.obtenerDatoAlumno()
                if opcion == 3:
                    alumnos.actualizarDatosAlumno()
                if opcion == 4:
                    alumnos.eliminarDatosAlumno()
                if opcion == 5:
                    alumnos.mostrarDatosGeneral()
                if opcion == 6:
                    os.system("cls")
                    menuTotal()
                if opcion == 7:
                    os.system("cls")
                    print("Te has desconectado...")
                    exit()
                    break
                if opcion != 7:
                    os.system("cls")
                    print(f"{opcion}: Numero no aceptado.")
            except ValueError:
                print("Error, solo elige la opcion en numeros")
        else:
            os.system("cls")
            print(f"\nERROR!, '{opcion}': No es una opcion correcta. Solo se permiten Digitos.\n")
            

def menuTotal():
    os.system("cls")
    print("\t\t\t\t//////////////////////////////////////////////////////////////////")
    print("\t\t\t\t****************** Bienvenidos a la Institucion ******************")
    print("\t\t\t\t//////////////////////////////////////////////////////////////////")
    print()
    while True:
        print("Usted es...")
        print("1.- Profesor")
        print("2.- Alumno")
        print("3.- Salir")
        opcion = input("Elegir una opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            try:
                if opcion == 1:
                    os.system("cls")
                    print("Acceso a Profesores")
                    Profes()
                    break    
                if opcion == 2:
                    os.system("cls")
                    print("Acceso a Alumnos")
                    Alumnos()
                    break   
                if opcion == 3:
                    os.system("cls")
                    print("Te has desconectado...")
                    exit()
                    break
            except ValueError:
                print("Error, solo elige la opcion en numeros")
        else:
            os.system("cls")
            print(f"\nERROR!, '{opcion}': No es una opcion correcta. Solo se permiten Digitos.\n")
            print("\t\t\t\t//////////////////////////////////////////////////////////////////")
            print("\t\t\t\t****************** Bienvenidos a la Institucion ******************")
            print("\t\t\t\t//////////////////////////////////////////////////////////////////")

#Pruebas
menuTotal()