# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

#    Un constructor, donde los datos pueden estar vacíos.
#    Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#    mostrar(): Muestra los datos de la persona.
#    esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

'''

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
            self.__dni = ''
    
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

persona = Persona('Alan', 27, '3964187')

print(persona.nombre) # GETTER

persona.nombre = 'Caca' # SETTER
print(persona.nombre)

'''

# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

#  Un constructor, donde los datos pueden estar vacíos.

#  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar diirectamente, sólo ingresando o retirando dinero.

#  mostrar(): Muestra los datos de la cuenta.

#  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa,   #    no se hará nada.

#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.



class Cuenta:

    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    
    def mostrar(self):
        return f'Nombre: {self.titular} - Cantidad: ${self.cantidad}'
    
    def ingresar(self, cantidad):
        cantidad = int(cantidad)
        if cantidad <= 0:
            return 'Cantidad incorrecta.'
        else:
            self.__cantidad += cantidad
            print('Dinero ingresado correctamente.')
            return f'Cantidad de dinero: ${self.cantidad}'
    
    def retirar(self, cantidad):
        cantidad = int(cantidad)
        if cantidad > self.cantidad:
            print('Dinero insuficiente.')
        else:
            print('Dinero retirado correctamente.')
            self.__cantidad -= cantidad
        return f'Cantidad de dinero: ${self.cantidad}'

alan = Cuenta('Alan Omes')
alan.cantidad = 500

#num = 1
# while num != 0:
    
#     print('\nBIENVENIDO. SELECCIONE LA OPCIÓN QUE DESEE REALIZAR:\r\n ')
#     print('1) Mostrar datos de la cuenta\n2) Ingresar dinero\n3) Retirar dinero\n4) Finalizar\n')
#     opcion = int(input('Opción: '))

#     print('\r')

#     if opcion == 1:
#         print(alan.mostrar())
#     elif opcion == 2:
#         cant = input('Cantidad de dinero que quiere ingresar: ')
#         print(alan.ingresar(cant))
#     elif opcion == 3:
#         cant = input('Cantidad de dinero que quiere retiar: ')
#         print(alan.retirar(cant))
#     elif opcion == 4:
#         print('Programa finalizado. Muchas gracias.')
#         num = 0
#     else:
#         print('Opción incorrecta. Por favor, intentelo nuevamente.')
    






