import sys
sys.path.append("./.")
from pyl.conn import Coneccion

class Alumno():
    def __init__(self,codAlum,nombre,apellido,dni,edad,n1,n2,n3,n4,prom):
        self.codAlum = codAlum
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.n4=n4
        self.prom = prom

    def agregarAlumno(self):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['alumno']
            diccionario = {"codAlumno":self.codAlum,"nombre":self.nombre,"apellido":self.apellido,"dni":self.dni,"edad":self.edad,"notas":[{"nota1":self.n1,"nota2":self.n2,"nota3":self.n3,"nota4":self.n4,"promedio":self.prom}]}
            coleccion.insert_one(diccionario)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()

    def obtenerAlumno(self,codAlum):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['alumno']
            query = {"codAlumno":codAlum}
            for x in coleccion.find(query):
                print(x)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()

    def actualizarAlumno(self,codAlum):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['alumno']
            query = {"codAlumno":codAlum}
            queryset = {"$set":{"nombre":self.nombre,"apellido":self.apellido,"dni":self.dni,"edad":self.edad}}
            coleccion.update_one(query,queryset)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()


    def eliminarAlumno(self,codAlum):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['alumno']
            query = {"codAlumno":codAlum}
            coleccion.remove(query)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()
    
    def mostrarAlumno(self):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['alumno']
            for x in coleccion.find():
                print(x)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()


#PRUEBAS:
#agregar = Alumno("2","Jose","Bustamante","45872365","29","19","19","19","19","19")
#agregar.agregarAlumno()

#obtener = Alumno("","","","","","","","","","")
#obtener.obtenerAlumno(1)

#actualizar = Alumno("","Josue","Ramirez","24578691","29","","","","","")
#actualizar.actualizarAlumno(2)

#actualizarNota = Alumno("","","","","","15","18","16","14","15.75")
#actualizarNota.actualizarNotaAlumno(2)

#db.alumno.insert({"codAlumno":1,"nombre":"Magaly","apellido":"Churata","dni":48978521,"edad":29,"notas":[{"nota1":19,"nota2":19,"nota3":19,"nota4":19,"promedio":19}]})
#db.alumno.insert({"codAlumno":2,"nombre":"Jose","apellido":"Bustamante","dni":45872365,"edad":29,"notas":[{"nota1":16,"nota2":13,"nota3":14,"nota4":17,"promedio":15}]})