from logica.customService import CharacterService
##CONSIDERAR CREAR UN GESTOR DE OBJETOS JUGADORES Y OTROS TIPOS DE GESTORES
from pubsub import pub
class PersonalizacionBusinessDelegate:
    def __init__(self, serviceLookup=None,serviceType=None):
        pub.subscribe(self.searchCharacters,"CHARACTER-OBJECT")
        self.serviceLookup = PersonalizacionServiceLookup()
        self.serviceType = serviceType
        # self.jugador=None

        self.serviceLookup.registerService("PERSONAJE",CharacterService())


    # def setServiceLookup(self, service_lookup):
    #     self.service_lookup = service_lookup

    def setServiceType(self, service_type):
        self.serviceType = service_type
    def searchCharacters(self, msg):
        self.serviceType="PERSONAJE"
        print("asdasdasda",msg)
        self.getCharacters(msg)

    def getCharacters(self,id):
        print(self.serviceLookup,self.serviceType)
        if self.serviceLookup is not None and self.serviceType is not None:
            service = self.serviceLookup.getService(self.serviceType)
            if service is not None:
                result=service.getCharactersById(id)
                print("result: ",result)
                if result:
                    # self.jugador=result
                    print("Enviando datos a JugadorHandler....")
                    pub.sendMessage("CHARACTERS", msg=result)
                    
                
            
            else:
                print("El servicio solicitado no está disponible.")
        else:
            print("No se ha configurado el servicio o el mecanismo de lookup.")

class PersonalizacionServiceLookup:
    def __init__(self) -> None:
        self.services={}

    def registerService(self,serviceType, service):
        self.services[serviceType]=service
    def getService(self, serviceType):
        return self.services.get(serviceType)