class GameMasterModel():
    def __init__(self, IdGm, NombreUsuario, Apodo, Clave):
        self.__id = IdGm
        self.__nombreUsuario = NombreUsuario
        self.__apodo = Apodo
        self.__clave = Clave
    #Getters 
    def getId(self):
        return self.__idgm
    def getNombreUsuario(self):
        return self.__nombreUsuario
    def getApodo(self):
        return self.__apodo
    def getClave(self):
        return self.__clave
    #Setters
    def setId(self,IdGm):
        self.__id = IdGm
    def setNombreUsuario(self, NombreUsuario):
        self.__nombreUsuario = NombreUsuario
    def setApodo(self,Apodo):
        self.__apodo = Apodo
    def setClave(self,Clave):
        self.__clave = Clave