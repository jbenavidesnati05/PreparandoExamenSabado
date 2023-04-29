class Piloto:
    def __init__(self):
        self.__nombre= None
        self.__fechaNacimiento= None
        self.__salarioAnual= None
        self.__Pais= None
        
# __________________________________________________________    
@property
def nombre(self):
    return self.__nombre

@nombre.setter 
def nombre(self, dato):
    self.__nombre = dato 
# __________________________________________________________    
@property
def fechaNacimiento(self):
    return self.__fechaNacimiento

@fechaNacimiento.setter 
def fechaNacimiento(self, dato):
    self.__fechaNacimiento = dato 
# __________________________________________________________    
@property
def salarioAnual(self):
    return self.__salarioAnual

@salarioAnual.setter 
def salarioAnual(self, dato):
    self.__salarioAnual = dato 
# __________________________________________________________    
@property
def pais(self):
    return self.__pais

@pais.setter 
def pais(self, dato):
    self.__pais = dato 
# __________________________________________________________    