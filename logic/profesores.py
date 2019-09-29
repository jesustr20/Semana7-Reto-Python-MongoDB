import sys,os
sys.path.append("./.")
from inst.profesor import Profesor


def registroProfesores():
    os.system("cls")
    print("Registrar a un profesor: ")
    print()
    #Me mostrara la tabla para agregar el codigo que sigue
    print("Ingresar el codigo despues del codigo que sigue en la lista")
    mostrar = Profesor("","","","","")
    mostrar.mostrarDocente()
    print()
    codProf = int(input("Ingresar el codigo de registro: "))
    nombre = input("Ingrese sus nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    dni = int(input("Ingresar su DNI: "))
    edad = int(input("Ingresar su edad:"))
    #CONVIRTIENDO A ENTEROS Y MONGODB LOS TOME COMO ENTEROS
    codProf = int(codProf)
    dni = int(dni)
    edad = int(edad)
    agregar = Profesor(codProf,nombre,apellido,dni,edad)
    agregar.agregarDocente()

def obtenerDatoProfesor():
    os.system("cls")
    print("Elegir un numero de registro para visualizar")
    num = int(input("Numero de registro: ")) 
    mostrar = Profesor("","","","","")
    mostrar.obtenerDocente(num)

def actualizarDatosProfesor():
    os.system("cls")
    print("Elegir un numero de registro a actualizar")
    #Me mostrara la relacion de profesores y eligire una opcion a registrar
    mostrar = Profesor("","","","","")
    mostrar.mostrarDocente()
    print()
    codProf = int(input("Codigo del Profesor: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = int(input("Dni: "))
    edad = int(input("Edad: "))
    #CONVIRTIENDO A ENTEROS Y MONGODB LOS TOME COMO ENTEROS
    codProf = int(codProf)
    dni = int(dni)
    edad = int(edad)
    actualizar = Profesor("",nombre,apellido,dni,edad)
    actualizar.actualizarDocente(codProf)
    print()
    print("Datos actualizados...")
    print()
    mostrar = Profesor("","","","","")
    mostrar.mostrarDocente()


def eliminarDatosProfesor():
    os.system("cls")
    print()
    print("Eliminar registro de un Profesor")
    print()
    mostrar = Profesor("","","","","")
    mostrar.mostrarDocente()
    print()
    print("Elegir codigo a eliminar")
    codProf = int(input("Codigo: "))
    codProf = int(codProf)
    eliminar = Profesor("","","","","")
    print()
    print(f"Codigo eliminado: {codProf}")
    eliminar.obtenerDocente(codProf)
    eliminar.eliminarDocente(codProf)
    print()
    print("Registro Actualizado")
    print()
    mostrar = Profesor("","","","","")
    mostrar.mostrarDocente()


def mostrarDatosGeneral():
    print("Visualizacion de todos los datos de los Docentes")
    mostrar = Profesor("","","","","")
    mostrar.mostrarDocente()