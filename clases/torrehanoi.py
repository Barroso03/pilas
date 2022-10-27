class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Pila:
    def __init__(self):
        self.superior = None
    def apilar(self, dato):
        print(f"Agregando {dato} en la cima de la pila")
        # Si no hay datos, agregamos el valor en el elemento superior y regresamos
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo
    def hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            print(f"mover disco de {origen} a {destino}")
            return
        else:
            self.hanoi(n-1, origen, destino, auxiliar)
            print(f"Mueve el disco de la torre", {origen} ,"a la torre",{destino})
            self.hanoi(n-1, auxiliar, origen, destino)
            
    def imprimir(self):
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")