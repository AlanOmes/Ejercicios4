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

'''

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

alan = Cuenta('Alan Omes', 10000)



num = 1
while num != 0:
    
    print('\nBIENVENIDO. SELECCIONE LA OPCIÓN QUE DESEE REALIZAR:\r\n ')
    print('1) Mostrar datos de la cuenta\n2) Ingresar dinero\n3) Retirar dinero\n4) Finalizar\n')
    opcion = int(input('Opción: '))

    print('\r')

    if opcion == 1:
        print(alan.mostrar())
    elif opcion == 2:
        cant = input('Cantidad de dinero que quiere ingresar: ')
        print(alan.ingresar(cant))
    elif opcion == 3:
        cant = input('Cantidad de dinero que quiere retiar: ')
        print(alan.retirar(cant))
    elif opcion == 4:
        print('Programa finalizado. Muchas gracias.')
        num = 0
    else:
        print('Opción incorrecta. Por favor, intentelo nuevamente.')
    
'''

# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye los siguientes métodos para la clase:

#  Un constructor.

#  Los setters y getters para el nuevo atributo.

#  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

#  Además la retirada de dinero sólo se podrá hacer si el titular es válido.

#  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

# Piensa los métodos heredados de la clase madre que hay que reescribir.

'''

class CuentaJoven(Cuenta):

    def __init__(self, nombre, cantidad, bonificacion):
        super().__init__(nombre, cantidad)
        self.bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def esTitularValido(self, edad):
        if edad >= 18 and edad <= 25:
            return True
        return False

    def retirar(self, valido):
        cant = int(input('Cantidad de dinero que quiere retiar: '))
        if valido == True:
            return super().retirar(cant)
        else:
            return 'Para retirar dinero debe ser titular válido.'
    
    def mostrar(self):
        c_total = self.bonificacion * self.cantidad / 100
        return f'Cuenta joven: ${c_total}'

joven = CuentaJoven('Alan', 10000, 50)

#print(joven.retirar(joven.esTitularValido(19)))
print(joven.mostrar())

joven.bonificacion = 20
print(joven.mostrar())

'''

# Realice un programa que cree un objeto persona con datos leídos desde teclado. Luego muestre en consola la representación de ese objeto en formato string.

'''

class Persona:

    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def mostrar(self):
        return f'Mi nombre es {self.nombre}, mi DNI es {self.dni} y tengo {self.edad} años.'

nombre = input('Ingrese su nombre: ')
dni = input('Ingrese su número de DNI: ')
edad = input('Ingrese su edad: ')

persona = Persona(nombre, dni, edad)
print(persona.mostrar())

'''

# 