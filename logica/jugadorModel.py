

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
    

    def setNivelCuenta(self,nivelCuenta):
        self.__nivelCuenta=nivelCuenta
    
    def setApodo(self,apodo):
        self.__apodo = apodo

    # Otros
    def addOneCharacter(self, character):
        if len(self.__personajes)>=4:
            print("No puedes tener más personajes")
        else:
            self.__personajes.append(character)
        print("Añadiendo personajes....")
    def addManyCharacters(self,characters:list):
        self.__personajes=[]
        if (len(self.__personajes)+len(characters))>4:
            print("La cantidad excede los personajes permitidos")
        else:
            for character in characters:
                self.__personajes.append(character)
            print(f"Este jugador tiene {len(self.__personajes)} personajes")
