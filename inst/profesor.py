import sys
sys.path.append("./.")
from pyl.conn import Coneccion

class Profesor():
    def __init__(self, codProfe,nombre, apellido, dni, edad):
        self.codProfe = codProfe
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad


    def agregarDocente(self):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['profesor']
            diccionario = {"codProfe":self.codProfe,"nombre":self.nombre,"apellido":self.apellido,"dni":self.dni,"edad":self.edad}
            coleccion.insert_one(diccionario)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()

    def obtenerDocente(self,codProf):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['profesor']
            query = {"codProfe":codProf}
            for x in coleccion.find(query):
                print(x)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()

    def actualizarDocente(self,codProf):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['profesor']
            query = {"codProfe":codProf}
            queryset = {"$set":{"nombre":self.nombre,"apellido":self.apellido,"dni":self.dni,"edad":self.edad}}
            coleccion.update_one(query,queryset)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()

    def eliminarDocente(self,codProf):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['profesor']
            query = {"codProfe":codProf}
            coleccion.remove(query)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()

    def mostrarDocente(self):
        try:
            conexion = Coneccion()
            dbcliente = conexion.conectar()
            coleccion = dbcliente['profesor']
            for x in coleccion.find():
                print(x)
        except Exception as e:
            print(e)
        else:
            conexion.cerrar()


#PRUEBAS:
#agregar = Profesor("2","jesus","roncal","42536954","25")
#agregar.agregarDocente()

#obtener = Profesor("","","","","")
#obtener.obtenerDocente(1)

#mostrar =Profesor("","","","","")
#mostrar.mostrarDocente()


#print("**************************************")
#mostrar = Profesor("","","","","")
#mostrar.mostrarDocente()

