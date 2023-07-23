

class JugadorModel():
    def __init__(self,id,nombreUsuario,apodo,nivelCuenta,clave) -> None:
        self.__id=id
        self.__nombreUsuario=nombreUsuario
        self.__personajes=[]
        self.__apodo=apodo
        self.__nivelCuenta=nivelCuenta
        self.__clave=clave
    def getId(self):
        return self.__id
    def getNombreUsuario(self):
        return self.__nombreUsuario
    def getPersonajes(self):
        return self.__personajes
    def getNivelCuenta(self):
        return self.__nivelCuenta
    def getApodo(self):
        return self.__apodo
  
    def setId(self, id):
        self.__id = id
    def setNombreUsuario(self,username):
        self.__nombreUsuario=username
    def setPersonajes(self,personaje):
        if len(self.__personajes==4): #Arreglar esto
            return None    
        else:
            self.__personajes.append(personaje)

    def setNivelCuenta(self,nivelCuenta):
        self.__nivelCuenta=nivelCuenta
    
    def setApodo(self,apodo):
        self.__apodo = apodo

