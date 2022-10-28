#Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves y la debes de crear tu– de las que conocemos su nombre, largo, tripulación y cantidad de pasajeros#

# crea una lista de diccionarios con la información de cada nave
class StarWars():
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
    # crea una lista que coja todas las naves,lar,tripulacion y pasajeros
    def __str__(self):
        return f"Nombre: {self.nombre}, Largo: {self.largo}, Tripulacion: {self.tripulacion}, Pasajeros: {self.pasajeros}"
class Xwings(StarWars):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        super().__init__(nombre, largo, tripulacion, pasajeros)
        
    def __str__(self):
        return super().__str__() 
    def __repr__(self):
        return self.__str__()

class Estrelladelamuerte(StarWars):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        super().__init__(nombre, largo, tripulacion, pasajeros)
        
    def __str__(self):
        return super().__str__() 
    def __repr__(self):
        return self.__str__()
b = Estrelladelamuerte("Estrella de la muerte", 120000, 342953, 843342)
class Halconmilenario(StarWars):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        super().__init__(nombre, largo, tripulacion, pasajeros)
        
    def __str__(self):
        return super().__str__() 
    def __repr__(self):
        return self.__str__()   


class Maria(StarWars):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        super().__init__(nombre, largo, tripulacion, pasajeros)
        
    def __str__(self):
        return super().__str__() 
    def __repr__(self):
        return self.__str__()

class Ywing(StarWars):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        super().__init__(nombre, largo, tripulacion, pasajeros)
        
    def __str__(self):
        return super().__str__() 
    def __repr__(self):
        return self.__str__()

class Andrea(StarWars):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        super().__init__(nombre, largo, tripulacion, pasajeros)
        
    def __str__(self):
        return super().__str__() 
    def __repr__(self):
        return self.__str__()

class AT_ST(StarWars):
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        super().__init__(nombre, largo, tripulacion, pasajeros)
        
    def __str__(self):
        return super().__str__() 
    def __repr__(self):
        return self.__str__()
a = Xwings("X-Wing", 12.5, 1, 0)
b = Estrelladelamuerte("Estrella de la muerte", 120000, 342953, 843342)
c = Halconmilenario("Halcón Milenario", 20, 4, 6)
d = Maria("Maria", 20, 4, 6)
e = Ywing("Y-wing", 14, 1, 0)
f = Andrea("Andrea", 14, 45, 8)
g = AT_ST("AT-ST", 2, 1, 0)

# crea una lista que coja todas las naves,lar,tripulacion y pasajeros
def ordenr_navesalfabetico():
    lista = [a,b,c,d,e,f,g]
    lista.sort(key=lambda x: x.nombre)
    print(lista)

def ordenar_navesporlargo():
    lista = [a,b,c,d,e,f,g]
    lista.sort(key=lambda x: x.largo)
    print(lista)

#  mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
def mostrarinfo():
    lista = [a,b,c,d,e,f,g]
    for i in lista:
        if i.nombre == "Halcón Milenario" or i.nombre == "Estrella de la muerte":
            print(i)


def cinconavesconmaspasajeros():
    lista = [a,b,c,d,e,f,g]
    lista.sort(key=lambda x: x.pasajeros, reverse=True)
    print(lista[:5])

#  indicar cuál es la nave que requiere mayor cantidad de tripulación y que solo salga el nombre de la nave;
def navesconmayortripulacion():
    lista = [a,b,c,d,e,f,g]
    lista.sort(key=lambda x: x.tripulacion, reverse=True)
    print(lista[0].nombre)

# mostrar las naves que empiezen por la letra “AT” y solo muestre el nombre de la nave;
def navesempiezanporAT():
    lista = [a,b,c,d,e,f,g]
    for i in lista:
        if i.nombre.startswith("AT"):
            print(i.nombre)

# • listar todas las naves que pueden llevar seis o más pasajeros y solo muestre el nombre de la nave;
def navesconmasde6pasajeros():
    lista = [a,b,c,d,e,f,g]
    for i in lista:
        if i.pasajeros >= 6:
            print(i.nombre)

#mostrar toda la información de la nave más pequeña y la más grande
def navesmaspequeña():
    lista = [a,b,c,d,e,f,g]
    lista.sort(key=lambda x: x.largo)
    print(lista[0])

def navesmasgrande():
    lista = [a,b,c,d,e,f,g]
    lista.sort(key=lambda x: x.largo, reverse=True)
    print(lista[0])



    



    
       


        





        