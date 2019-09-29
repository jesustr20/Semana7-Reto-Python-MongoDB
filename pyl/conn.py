import pymongo

class Coneccion():
    def __init__(self,host="localhost",puerto="27017",db="Institucion"):
        self.host=host
        self.puerto = puerto
        self.db = db
        self.conexion = pymongo.MongoClient("mongodb://{}:{}/".format(self.host,self.puerto))
        self.cliente = self.conexion[self.db]

    def conectar(self):
        return self.cliente
    
    def cerrar(self):
        self.conexion.close()

#PRUEBAS
#conectar = Coneccion()