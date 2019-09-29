import sys,os
sys.path.append("./.")
from inst.alumno import Alumno

#YA ESTA
def registroAlumnos():
    os.system("cls")
    print("Registrar a un Alumno: ")
    print()
    #Me mostrara la tabla para agregar el codigo que sigue
    print("Ingresar el codigo despues del codigo que sigue en la lista")
    mostrar = Alumno("","","","","","","","","","")
    mostrar.mostrarAlumno()
    print()
    codAlumno = int(input("Ingresar el codigo de registro: "))
    nombre = input("Ingrese sus nombre: ")
    apellido = input("Ingrese sus apellidos: ")
    dni = int(input("Ingresar su DNI: "))
    edad = int(input("Ingresar su edad: "))
    #Diccionario
    print("Ingresar Notas")
    notas = []
    for n in range(1,5):
        nota = input(f"Nota Nro {n}: ")
        notas.append(nota)
    n1 = int(notas[0])
    n2 = int(notas[1])
    n3 = int(notas[2])
    n4 = int(notas[3])
    prom = (n1+n2+n3+n4)/4
    prome = prom
    #CONVIRTIENDO A ENTEROS Y MONGODB LOS TOME COMO ENTEROS
    codAlumno = int(codAlumno)
    dni = int(dni)
    edad = int(edad)
    agregar = Alumno(codAlumno,nombre,apellido,dni,edad,n1,n2,n3,n4,prome)
    agregar.agregarAlumno()
    #print()
    print("Registro con Exito")
    #print()
    #agregar.mostrarAlumno()

#Ya esta
def obtenerDatoAlumno():
    os.system("cls")
    print("Elegir un numero de registro para visualizar")
    num = int(input("Numero de registro: ")) 
    mostrar = Alumno("","","","","","","","","","")
    mostrar.obtenerAlumno(num)

#YA ESTA
def actualizarDatosAlumno():
    os.system("cls")
    print("Elegir un numero de registro a actualizar")
    #Me mostrara la relacion de profesores y eligire una opcion a registrar
    mostrar = Alumno("","","","","","","","","","")
    mostrar.mostrarAlumno()
    print()
    codAlumno = int(input("Codigo del Alumno: "))
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = int(input("Dni: "))
    edad = int(input("Edad: "))
    #CONVIRTIENDO A ENTEROS Y MONGODB LOS TOME COMO ENTEROS
    dni = int(dni)
    edad = int(edad)
    actualizar = Alumno("",nombre,apellido,dni,edad,"","","","","")
    actualizar.actualizarAlumno(codAlumno)
    print()
    print("Datos actualizados...")
    print()
    mostrar = Alumno("","","","","","","","","","")
    mostrar.mostrarAlumno()


def eliminarDatosAlumno():
    os.system("cls")
    print()
    print("Eliminar registro del Alumno")
    print()
    mostrar = Alumno("","","","","","","","","","")
    mostrar.mostrarAlumno()
    print()
    print("Elegir codigo a eliminar")
    codAlumn = int(input("Codigo: "))
    codAlumn = int(codAlumn)
    eliminar = Alumno("","","","","","","","","","")
    print()
    print(f"Codigo eliminado: {codAlumn}")
    eliminar.obtenerAlumno(codAlumn)
    eliminar.eliminarAlumno(codAlumn)
    print()
    print("Registro Actualizado")
    print()
    mostrar = Alumno("","","","","","","","","","")
    mostrar.mostrarAlumno()

#Ya esta
def mostrarDatosGeneral():
    print("Visualizacion de todos los datos de los Docentes")
    mostrar = Alumno("","","","","","","","","","")
    mostrar.mostrarAlumno()