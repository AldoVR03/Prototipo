from logica.userService import JugadorService, GmService
##CONSIDERAR CREAR UN GESTOR DE OBJETOS JUGADORES Y OTROS TIPOS DE GESTORES
class InicioBusinessDelegate:
    def __init__(self, serviceLookup=None,serviceType=None):
        self.serviceLookup = ServiceLookup()
        self.serviceType = serviceType
        self.jugador=None
        self.serviceLookup.registerService("JUGADOR",JugadorService())
        self.serviceLookup.registerService("GM",GmService())

    # def setServiceLookup(self, service_lookup):
    #     self.service_lookup = service_lookup

    def setServiceType(self, service_type):
        self.serviceType = service_type

    def checkUser(self, username,password):
        print(self.serviceLookup,self.serviceType)
        if self.serviceLookup is not None and self.serviceType is not None:
            service = self.serviceLookup.getService(self.serviceType)
            if service is not None:
                result=service.checkUser(username,password)
                self.jugador=result[1]
                return result[0]
            
            else:
                print("El servicio solicitado no está disponible.")
        else:
            print("No se ha configurado el servicio o el mecanismo de lookup.")

    def hasCharacter(self):
        service=self.serviceLookup.getService(self.serviceType)
        return service.checkCharacter(self.jugador.id)
    def checkRegisterUser(self, username, nickname):
        if self.serviceLookup is not None and self.serviceType is not None:
            service = self.serviceLookup.getService(self.serviceType)
            if service is not None:
                result=service.checkUserRegister(username,nickname) 
                return result
            
            else:
                print("El servicio solicitado no está disponible.")
        else:
            print("No se ha configurado el servicio o el mecanismo de lookup.")
    
    def registerUser(self, username, nickname,password):
        if self.serviceLookup is not None and self.serviceType is not None:
            service = self.serviceLookup.getService(self.serviceType)
            if service is not None:
                result=service.registerUser(username,nickname, password) 
                return result
            
            else:
                print("El servicio solicitado no está disponible.")
        else:
            print("No se ha configurado el servicio o el mecanismo de lookup.")
class ServiceLookup:
    def __init__(self) -> None:
        self.services={}

    def registerService(self,serviceType, service):
        self.services[serviceType]=service
    def getService(self, serviceType):
        return self.services.get(serviceType)