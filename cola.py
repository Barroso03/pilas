class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Cola:
    def __init__(self):
        self.items=[]
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
    #""" Elimina el primer elemento de la cola y devuelve su
       # valor. Si la cola está vacía, levanta ValueError. """
        try:
           return self.items.pop(0)
        except:
           raise ValueError("La cola está vacía")
    def es_vacia(self):
        return self.items == []
q = Cola()
q.encolar(3)
q.encolar(23)
q.desencolar()

         
 # 1.torre de hanoi recursivo,2.Regla de sarrows recursivo e iterativo sin librerias,3.poo,4.TDA polinomio con linkelist,5.doble tabla hash