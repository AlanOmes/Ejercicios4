# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

#    Un constructor, donde los datos pueden estar vacíos.
#    Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#    mostrar(): Muestra los datos de la persona.
#    esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    
    def __init__(self, nombre = '', edad = 0, dni = ''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property        
    def validar_dni(self):
        if len(self.__dni) != 8:
            print('DNI incorrecto')
    
    @dni.setter
    def dni(self, dni):
        self.__dni = dni
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    def mostrar(self):
        return f'Nombre: {self.nombre} - Edad: {self.edad} - DNI: {self.dni}'
    
    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return True
        return False