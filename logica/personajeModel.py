
class PersonajeModel():
    def __init__(self, id,idClan,nombrePersonaje,raza,clase,nivelPersonaje,vida,ataque,defensa,velocidad,monedas,expPersonaje,hairColor,skinColor,eyeColor) -> None:
          self.__id=id
          self.__idClan=idClan
          self.__nombrePersonaje=nombrePersonaje
          self.__raza=raza
          self.__clase=clase
          self.__nivelPersonaje=nivelPersonaje
          self.__vida=vida
          self.__ataque=ataque
          self.__defensa=defensa
          self.__velocidad=velocidad
          self.__monedas=monedas
          self.__expPersonaje=expPersonaje
          self.__hairColor=hairColor
          self.__skinColor=skinColor
          self.__eyeColor=eyeColor

  # GETTERS
    def getId(self):
         return self.__id
    def getIdClan(self):
         return self.__idClan
    def getNombrePersonaje(self):
         return self.__nombrePersonaje
    def getRaza(self):
         return self.__clase
    def getClase(self):
         return self.__nivelPersonaje
    
    def getNivelPersonaje(self):
         return self.__vida
    def getVida(self):
         return self.__vida
    def getAtaque(self):
         return self.__vida
    def getDefensa(self):
         return self.__defensa
    def getVelocidad(self):
         return self.__velocidad
    
    def getMonedas(self):
         return self.__monedas
    def getExpPersonaje(self):
         return self.__expPersonaje
    def getHairColor(self):
         return self.__hairColor
    def getSkinColor(self):
         return self.__skinColor
    def getEyeColor(self):
         return self.__eyeColor
    
  # SETTERS
    def setId(self, id):
         self.__id=id
    def setNombrePersonaje(self, nom):
         self.__nombrePersonaje=nom
    def setIdClan(self, idClan):
         self.__idClan=idClan
    def setRaza(self, raza):
         self.__raza=raza
    def setClase(self, clase):
         self.__clase=clase

    def setNivelPersonaje(self, nivelPersonaje):
         self.__nivelPersonaje=nivelPersonaje
    def setVida(self, vida):
         self.__vida=vida
    def setAtaque(self, ataque):
         self.__ataque=ataque
    def setDefensa(self, defensa):
         self.__defensa=defensa
    def setVelocidad(self, vel):
         self.__velocidad=vel
    
    def setMonedas(self, monedas):
         self.__monedas=monedas
    def setExpPersonaje(self, exp):
         self.__expPersonaje=exp
    def setHairColor(self, hc):
         self.__hairColor=hc
    def setSkinColor(self, sc):
         self.__skinColor=sc
    def setEyeColor(self, ec):
         self.__eyeColor=ec
    
          
    
    